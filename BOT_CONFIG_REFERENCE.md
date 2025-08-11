# FlexPay Sim.ai Bot Configuration Reference

## Bot Architecture Overview

The `Flex-io.yaml` defines a 3-block workflow:

```
[Start] → [Knowledge Query] → [Summary Agent] → [Response]
```

## Block Details

### 1. Start Block (`90fbac6c-081b-42a2-a827-b045a902a56c`)
- **Type**: starter
- **Name**: Start
- **Function**: Initiates chat workflow and captures user input
- **Output**: Passes user input to knowledge search

### 2. Knowledge Query Block (`1fdfe4a4-3395-484c-8f51-c990fe80e52e`)
- **Type**: knowledge
- **Name**: Query Search
- **Operation**: search
- **Knowledge Base ID**: `f6eb8f70-4807-4499-bc79-e4c77f09bd0e`
- **Query Source**: `<start.input>` (user's question)
- **Results**: Top 5 most relevant matches (`topK: '5'`)

### 3. Summary Agent Block (`f2515322-b086-47a8-b36d-19e596fc3f68`)
- **Type**: agent
- **Name**: Summary Agent
- **Model**: Gemini 2.5 Flash
- **Temperature**: 0.7
- **API Key**: `{{GOOGLE_GEMINI_API_KEY}}`

## System Prompt Template

The bot uses this system prompt structure:

```
You are an AI assistant tasked with answering user questions using the most relevant verified reference information provided to you.

Goals:
- Produce clear, professional, well-formatted answers
- Summarize, list, or explain as needed
- Never invent details outside provided references
- Include direct links exactly as provided
- Use formatting for readability

Response Format:
- Start with brief direct answer
- Present supporting details in readable structure
- List multiple resources with descriptions
- State clearly if information is not available
```

## User Prompt Template

```
User Query: <start.input>
Database Results: <querysearch.results>
```

## Knowledge Base Schema

The `all_data.csv` contains:
- **url**: Source webpage URL
- **filename**: Generated filename
- **title**: Page title
- **summary**: Content summary
- **content_type**: Classification
- **importance_score**: Relevance score (1-10)
- **key_points**: Key takeaways

## Required Environment Variables

- `GOOGLE_GEMINI_API_KEY`: Your Gemini API key from Google AI Studio

## Configuration Notes

- The knowledge base ID in the YAML must match your Sim.ai knowledge base
- The bot is optimized for FlexPay-related queries
- Temperature of 0.7 balances accuracy and natural language
- Top-K of 5 provides sufficient context without overwhelming the model
