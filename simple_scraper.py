import os
import asyncio
import json
import csv
import google.generativeai as genai
from crawl4ai import AsyncUrlSeeder, AsyncWebCrawler, SeedingConfig, BrowserConfig, CrawlerRunConfig, CacheMode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from environment variables
BASE_URL = os.getenv('BASE_URL', 'flexpay.io')
TEST_PAGES_LIMIT = int(os.getenv('TEST_PAGES_LIMIT')) if os.getenv('TEST_PAGES_LIMIT') else None
OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'output')
HEADLESS_MODE = os.getenv('HEADLESS_MODE', 'true').lower() == 'true'
CRAWLER_CONCURRENCY = int(os.getenv('CRAWLER_CONCURRENCY', '20'))
CRAWLER_HITS_PER_SEC = int(os.getenv('CRAWLER_HITS_PER_SEC', '10'))
SCRAPE_DELAY = float(os.getenv('SCRAPE_DELAY', '0.5'))
GEMINI_DELAY = float(os.getenv('GEMINI_DELAY', '4'))
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash-lite')
GEMINI_TEMPERATURE = float(os.getenv('GEMINI_TEMPERATURE', '0.1'))
GEMINI_MAX_TOKENS = int(os.getenv('GEMINI_MAX_TOKENS', '1000'))

METADATA_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "Main title of the page"},
        "summary": {"type": "string", "description": "2-3 sentence summary"},
        "content_type": {"type": "string", "description": "Type: feature, pricing, about, documentation, product, other"},
        "importance_score": {"type": "integer", "description": "Importance 1-10 for chatbot context", "minimum": 1, "maximum": 10},
        "key_points": {"type": "array", "items": {"type": "string"}, "description": "3-5 key points or features"}
    },
    "required": ["title", "summary", "content_type", "importance_score"]
}

async def get_all_urls():
    config = SeedingConfig(
        source="sitemap",
        max_urls=-1,
        concurrency=CRAWLER_CONCURRENCY,
        hits_per_sec=CRAWLER_HITS_PER_SEC
    )
    
    async with AsyncUrlSeeder() as seeder:
        urls = await seeder.urls(BASE_URL, config)
        return [url['url'] if isinstance(url, dict) else url for url in urls]

async def scrape_to_markdown(urls):
    browser_cfg = BrowserConfig(headless=HEADLESS_MODE)
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    
    markdown_data = []
    
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] Getting markdown: {url}")
            
            result = await crawler.arun(url=url, config=crawl_config)
            
            if result.success and result.markdown:
                markdown_data.append({
                    'url': url,
                    'markdown': str(result.markdown)
                })
            
            await asyncio.sleep(SCRAPE_DELAY)
    
    return markdown_data

async def extract_metadata_with_gemini(markdown_data):
    # Configure Gemini
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel(GEMINI_MODEL)
    
    results = []
    
    for i, item in enumerate(markdown_data, 1):
        print(f"[{i}/{len(markdown_data)}] Extracting metadata: {item['url']}")
        
        try:
            # Create prompt for Gemini
            prompt = f"""
Extract metadata from this FlexPay webpage content and return ONLY a valid JSON object with no additional text or formatting.

URL: {item['url']}

Markdown Content:
{item['markdown'][:8000]}  

Return JSON with this exact structure:
{{
    "title": "Main title of the page",
    "summary": "2-3 sentence summary of the content",
    "content_type": "Type: feature, pricing, about, documentation, product, other",
    "importance_score": 7,
    "key_points": ["key point 1", "key point 2", "key point 3"]
}}

Requirements:
- title: Extract the main page title
- summary: Write 2-3 sentences summarizing the page content
- content_type: Classify as one of: feature, pricing, about, documentation, product, other
- importance_score: Rate 1-10 for chatbot context relevance (10 = most important)
- key_points: List 3-5 most important points or features

Return ONLY the JSON object, no other text.
"""
            
            # Call Gemini API
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=GEMINI_TEMPERATURE,
                    max_output_tokens=GEMINI_MAX_TOKENS,
                )
            )
            
            # Parse response
            response_text = response.text.strip()
            
            # Clean up response - remove markdown code blocks if present
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.startswith('```'):
                response_text = response_text[3:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            
            response_text = response_text.strip()
            
            # Parse JSON
            metadata = json.loads(response_text)
            
            results.append({
                'url': item['url'],
                'markdown': item['markdown'],
                'metadata': metadata
            })
            
            print(f"    ✅ {metadata.get('title', 'Unknown')} (Score: {metadata.get('importance_score', 'N/A')}/10)")
            
            # Rate limit delay from environment variable
            await asyncio.sleep(GEMINI_DELAY)
            
        except json.JSONDecodeError as e:
            print(f"    ❌ JSON parsing error: {e}")
            print(f"    Response: {response_text[:200]}...")
            await asyncio.sleep(GEMINI_DELAY)
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            await asyncio.sleep(GEMINI_DELAY)
    
    return results

def save_results(results):
    # Create separate folders for markdown and JSON files
    os.makedirs(f"{OUTPUT_DIR}/markdown", exist_ok=True)
    os.makedirs(f"{OUTPUT_DIR}/json", exist_ok=True)
    
    # Save individual files
    for i, result in enumerate(results, 1):
        url_path = result['url'].replace(f'https://{BASE_URL}/', '').replace(f'https://{BASE_URL}', '') or 'homepage'
        filename = url_path.replace('/', '_').replace('?', '_').replace('#', '_')[:30]
        
        # Save markdown
        with open(f"{OUTPUT_DIR}/markdown/{i:03d}_{filename}.md", 'w', encoding='utf-8') as f:
            f.write(f"# {result['metadata'].get('title', 'Page Content')}\n\n")
            f.write(f"**URL:** {result['url']}\n")
            f.write(f"**Type:** {result['metadata'].get('content_type', 'unknown')}\n")
            f.write(f"**Score:** {result['metadata'].get('importance_score', 'N/A')}/10\n\n")
            f.write("---\n\n")
            f.write(result['markdown'])
        
        # Save metadata
        with open(f"{OUTPUT_DIR}/json/{i:03d}_{filename}_meta.json", 'w', encoding='utf-8') as f:
            json.dump({
                'url': result['url'],
                'filename': f"{i:03d}_{filename}.md",
                **result['metadata']
            }, f, indent=2)
    
    # Save consolidated data in JSON folder
    with open(f"{OUTPUT_DIR}/json/all_data.json", 'w', encoding='utf-8') as f:
        json.dump({
            'total_pages': len(results),
            'pages': [{
                'url': r['url'],
                'filename': f"{i:03d}_{r['url'].replace(f'https://{BASE_URL}/', '').replace(f'https://{BASE_URL}', '') or 'homepage'}".replace('/', '_').replace('?', '_').replace('#', '_')[:30] + '.md',
                **r['metadata']
            } for i, r in enumerate(results, 1)]
        }, f, indent=2)
    
    # Save as CSV
    with open(f"{OUTPUT_DIR}/all_data.csv", 'w', newline='', encoding='utf-8') as f:
        if results:
            # Get all possible keys from metadata
            fieldnames = ['url', 'filename', 'title', 'summary', 'content_type', 'importance_score', 'key_points']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for i, result in enumerate(results, 1):
                url_path = result['url'].replace(f'https://{BASE_URL}/', '').replace(f'https://{BASE_URL}', '') or 'homepage'
                filename = url_path.replace('/', '_').replace('?', '_').replace('#', '_')[:30]
                
                # Convert key_points list to comma-separated string for CSV
                key_points_str = '; '.join(result['metadata'].get('key_points', [])) if result['metadata'].get('key_points') else ''
                
                writer.writerow({
                    'url': result['url'],
                    'filename': f"{i:03d}_{filename}.md",
                    'title': result['metadata'].get('title', ''),
                    'summary': result['metadata'].get('summary', ''),
                    'content_type': result['metadata'].get('content_type', ''),
                    'importance_score': result['metadata'].get('importance_score', ''),
                    'key_points': key_points_str
                })

async def main():
    print("FlexPay Scraper - Lean & Clean")
    print("=" * 35)
    
    # Step 1: Get all URLs
    print("🔍 Getting all URLs from sitemap...")
    urls = await get_all_urls()
    print(f"✅ Found {len(urls)} URLs")
    
    # Apply test limit
    if TEST_PAGES_LIMIT and len(urls) > TEST_PAGES_LIMIT:
        urls = urls[:TEST_PAGES_LIMIT]
        print(f"🧪 Testing with first {len(urls)} URLs")
    
    # Step 2: Convert to markdown
    print("\n📝 Converting to markdown...")
    markdown_data = await scrape_to_markdown(urls)
    print(f"✅ Converted {len(markdown_data)} pages")
    
    # Step 3: Extract metadata with Gemini
    print("\n🧠 Extracting metadata with Gemini...")
    print(f"⏱️ Rate limit: {GEMINI_DELAY}s delays (~{len(markdown_data) * GEMINI_DELAY / 60:.1f} minutes)")
    results = await extract_metadata_with_gemini(markdown_data)
    
    # Step 4: Save results
    print(f"\n💾 Saving {len(results)} results...")
    save_results(results)
    
    print(f"\n✅ Complete! Processed {len(results)} pages")
    print(f"📁 Output: ./{OUTPUT_DIR}/ folder")

if __name__ == "__main__":
    asyncio.run(main())
