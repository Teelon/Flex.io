# FlexPay AI Assistant: Complete Knowledge Base & Bot Solution

> **Job Application Portfolio Project**  
> A full-stack AI solution demonstrating web scraping, data processing, AI integration, and chatbot deployment capabilities.

## 📋 Project Overview

This project showcases a complete pipeline for creating and deploying an AI-powered knowledge assistant:

1. **[Web Scraping](#-web-scraping-pipeline)** - Intelligent site crawling and content extraction
2. **[AI Processing](#-ai-powered-analysis)** - Content analysis using Google Gemini API
3. **[Data Pipeline](#-data-processing)** - Structured output generation for AI systems
4. **[Bot Deployment](#-ready-to-deploy-bot)** - Production-ready Sim.ai bot configuration

**Key Technologies:** Python, Crawl4AI, Google Gemini API, Sim.ai, CSV/JSON data processing

## 📁 Project Structure & Documentation

```
├── 📄 README.md                          # This overview (you are here)
├── 🔧 simple_scraper.py                  # Main scraping application
├── 🔧 json_to_csv_converter.py           # Data processing utility
├── 🤖 Flex-io.yaml                       # Sim.ai bot configuration
├── 📚 SIM_AI_SETUP_GUIDE.md             # → Complete bot deployment guide
├── 📚 BOT_CONFIG_REFERENCE.md           # → Technical bot configuration details
├── 📦 requirements.txt                   # Python dependencies
├── 📊 output/
│   ├── all_data.csv                      # → Final knowledge base (46+ pages)
│   ├── all_data.json                     # JSON format knowledge base
│   ├── combined_metadata.csv             # Metadata compilation
│   ├── json/                             # Individual page metadata
│   └── markdown/                         # Clean content in markdown format
```

**📖 Key Documentation:**
- **[Sim.ai Bot Deployment Guide](SIM_AI_SETUP_GUIDE.md)** - Step-by-step bot setup instructions
- **[Bot Configuration Reference](BOT_CONFIG_REFERENCE.md)** - Technical implementation details

## 🚀 Quick Deploy: Ready-to-Use AI Assistant

**Want to see the end result?** Deploy the pre-built FlexPay AI assistant in minutes:

1. **Get Started**: Follow **[SIM_AI_SETUP_GUIDE.md](SIM_AI_SETUP_GUIDE.md)**
2. **Use These Files**:
   - `Flex-io.yaml` - Complete bot workflow
   - `output/all_data.csv` - Knowledge base (46+ pages)
3. **Requirements**: Gemini API key + Sim.ai account

The deployed bot can answer questions about FlexPay's products, services, payment recovery, and industry solutions.

---

## 🛠 Technical Implementation

### 🔍 Web Scraping Pipeline

**Automated Site Discovery**
- Parses FlexPay's sitemap for comprehensive page discovery
- Intelligent URL filtering to focus on content pages
- Metadata extraction during discovery phase
- **Result**: 46+ pages successfully identified and processed

**Content Processing**
- Clean HTML to Markdown conversion using Crawl4AI
- Noise removal (navigation, footers, ads, scripts)
- Structural preservation of headings, links, and key elements
- Content quality filtering for AI processing

### 🧠 AI-Powered Analysis

**Google Gemini Integration**
- Uses Gemini Pro API for intelligent content analysis
- Structured metadata extraction optimized for chatbots
- Batch processing with rate limiting and error handling

**Generated Metadata Schema**
```json
{
  "title": "Clear, concise page title",
  "summary": "AI-generated page summary", 
  "content_type": "feature|pricing|about|documentation|blog",
  "importance_score": "1-10 relevance rating",
  "key_points": ["Main takeaway 1", "Main takeaway 2", "..."],
  "target_audience": "developers|businesses|general"
}
```

### 📊 Data Processing Pipeline

**Multi-Format Output Generation**
- **JSON Files**: Individual page metadata (`output/json/`)
- **Markdown Files**: Clean content format (`output/markdown/`)
- **CSV Database**: Consolidated knowledge base (`output/all_data.csv`)
- **Combined Metadata**: Aggregated insights (`output/combined_metadata.csv`)

**Data Quality Features**
- Importance scoring for content relevance
- Structured key points extraction
- Content type categorization
- URL and filename mapping

### 🤖 Ready-to-Deploy Bot

**Sim.ai Integration** ([Setup Guide](SIM_AI_SETUP_GUIDE.md))
- Pre-configured bot workflow (`Flex-io.yaml`)
- 3-stage processing: Input → Knowledge Search → AI Response
- Gemini 2.5 Flash integration for natural language responses
- Professional response formatting with citations

**Bot Architecture** ([Technical Details](BOT_CONFIG_REFERENCE.md))
```
User Query → Knowledge Base Search → AI Processing → Formatted Response
     ↓              ↓                      ↓              ↓
  Chat UI      CSV Database          Gemini 2.5     Professional
            (46+ FlexPay pages)      Flash API        Answer
```

---

## 🚧 Development Setup

**Environment Setup**
- Python 3.8+ (3.9+ recommended for best compatibility)
- Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Virtual environment (strongly recommended)

**Quick Installation**
```powershell
# Clone and setup
git clone <repository-url>
cd "Flex.io"

# Virtual environment setup
python -m venv .venv
.venv\Scripts\activate.bat  # Windows
# source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
crawl4ai-setup
```

**Environment Configuration**
```powershell
# Set Gemini API key
set GEMINI_API_KEY=your_actual_gemini_api_key_here
```
```cmd
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat
```

#### On macOS/Linux:
```bash
# Create virtual environment
### 🔧 Core Applications

#### 1. `simple_scraper.py` - Main Intelligence Engine

**Primary scraping application with AI-powered analysis**

```bash
python simple_scraper.py
```

**Key Features:**
- ✅ Automated sitemap discovery and URL extraction  
- ✅ Asynchronous crawling with rate limiting
- ✅ Clean markdown conversion with noise filtering
- ✅ AI metadata extraction using Gemini Pro API
- ✅ Real-time progress tracking and ETA calculations
- ✅ Structured JSON/CSV output for downstream systems

**AI Processing Capabilities:**
- Content analysis and summarization
- Importance scoring (1-10 scale)
- Content type classification
- Key insights extraction
- Chatbot-optimized metadata generation

#### 2. `json_to_csv_converter.py` - Data Pipeline Utility

**Consolidates JSON metadata into structured CSV database**

```bash
python json_to_csv_converter.py
```

**Features:**
- ✅ Batch JSON to CSV conversion
- ✅ Data validation and integrity checking
- ✅ Nested data structure handling
- ✅ Database-ready output format

---

## 📊 Results & Performance

**Scraped Data Summary:**
- **46+ pages** successfully processed
- **100% success rate** on content extraction
- **Rich metadata** generated for each page
- **Multi-format outputs** (JSON, CSV, Markdown)

**Sample Output Structure:**
```csv
url,title,summary,content_type,importance_score,key_points
https://flexpay.io/blog/...,Page Title,AI Summary,blog,8,"Key point 1; Key point 2"
```

**Performance Metrics:**
- Average processing: ~30 seconds per page (including AI analysis)
- Memory efficient: <2GB RAM usage
- API compliant: Built-in rate limiting for Gemini API

---

## 🎯 Skills Demonstrated

**Technical Skills:**
- **Python Development**: Async programming, API integration, data processing
- **AI/ML Integration**: Google Gemini API, prompt engineering, structured outputs
- **Web Scraping**: Advanced crawling techniques, content extraction, rate limiting
- **Data Engineering**: JSON/CSV processing, data validation, pipeline creation
- **Bot Development**: Sim.ai integration, workflow configuration, deployment

**Software Engineering Practices:**
- Clean, modular code architecture
- Comprehensive error handling and logging
- Environment configuration management
- Documentation and user guides
- Testing and validation workflows

---

## 📚 Additional Resources

**Complete Documentation:**
- **[Sim.ai Bot Deployment Guide](SIM_AI_SETUP_GUIDE.md)** - Production deployment instructions
- **[Bot Configuration Reference](BOT_CONFIG_REFERENCE.md)** - Technical implementation details
- **[Requirements Documentation](requirements.txt)** - Complete dependency list

**Output Files:**
- **[Knowledge Base CSV](output/all_data.csv)** - Final consolidated database
- **[Individual Metadata](output/json/)** - Per-page analysis results  
- **[Clean Content](output/markdown/)** - Processed markdown files

---

## 🚀 Deployment Ready

This project includes everything needed for production deployment:

1. **✅ Scraped Knowledge Base** - 46+ pages of structured FlexPay data
2. **✅ AI Bot Configuration** - Ready-to-import Sim.ai workflow  
3. **✅ Deployment Documentation** - Step-by-step setup guides
4. **✅ Data Processing Pipeline** - Automated conversion utilities

**Next Steps for Production:**
1. Follow [SIM_AI_SETUP_GUIDE.md](SIM_AI_SETUP_GUIDE.md) for bot deployment
2. Configure monitoring and analytics
3. Set up automated data refresh workflows
4. Integrate with existing customer service systems

---

## 💡 Project Highlights

**Problem Solved:** Created an end-to-end solution for converting website content into an intelligent AI assistant, demonstrating skills in web scraping, AI integration, data processing, and bot deployment.

**Technologies Used:** Python, Crawl4AI, Google Gemini API, Sim.ai, CSV/JSON data processing, async programming, API rate limiting, markdown processing.

**Business Value:** Automated knowledge base creation and AI assistant deployment that could serve customer inquiries 24/7 with accurate, up-to-date information about FlexPay's products and services.
