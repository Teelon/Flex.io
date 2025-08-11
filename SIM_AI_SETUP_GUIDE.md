# Sim.ai Bot Setup Guide for FlexPay Assistant

This guide will walk you through setting up a FlexPay knowledge assistant using Sim.ai with the provided `Flex-io.yaml` configuration file and scraped data.

## Prerequisites

- A Gemini API key from Google AI Studio
- The `all_data.csv` file containing FlexPay scraped data
- The `Flex-io.yaml` bot configuration file

## Step 1: Create a Sim.ai Account

1. Visit [sim.ai](https://sim.ai)
2. Click "Sign Up" to create a new account
3. Complete the registration process with your email and password
4. Verify your email address if required
5. Log in to your new Sim.ai account

## Step 2: Set Up Your Gemini API Key

### Get Your Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API key" in the left sidebar
4. Click "Create API key in new project" (or select an existing project)
5. Copy the generated API key

### Set Environment Variable
Set the `GOOGLE_GEMINI_API_KEY` environment variable:

**Windows (PowerShell):**
```powershell
[Environment]::SetEnvironmentVariable("GOOGLE_GEMINI_API_KEY", "YOUR_API_KEY_HERE", "User")
```

**Windows (Command Prompt):**
```cmd
setx GOOGLE_GEMINI_API_KEY "YOUR_API_KEY_HERE"
```

**Linux/macOS:**
```bash
export GOOGLE_GEMINI_API_KEY="YOUR_API_KEY_HERE"
# Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export GOOGLE_GEMINI_API_KEY="YOUR_API_KEY_HERE"' >> ~/.bashrc
```

## Step 3: Create a New Project in Sim.ai

1. From your Sim.ai dashboard, click "Create New Project" or "New Project"
2. Enter a project name (e.g., "FlexPay Assistant")
3. Optionally add a description: "AI assistant for FlexPay information and support"
4. Click "Create Project"

## Step 4: Import the Bot Configuration

1. In your new project, look for an "Import" or "Upload Configuration" option
2. Click "Import YAML" or similar option
3. Upload the `Flex-io.yaml` file from your project directory
4. The system should automatically parse and load the bot configuration with:
   - **Start block**: Initiates chat workflow
   - **Knowledge Query block**: Searches the knowledge base
   - **Summary Agent block**: Processes results using Gemini 2.5 Flash

## Step 5: Create and Configure Knowledge Base

### Upload Your Data
1. Navigate to the "Knowledge Base" or "Data Sources" section
2. Click "Create New Knowledge Base" or "Add Knowledge Base"
3. Name it appropriately (e.g., "FlexPay Content Database")
4. Upload the `all_data.csv` file from the `output/` directory

### Configure Knowledge Base Settings
The CSV file contains the following columns that Sim.ai can use:
- **url**: Source URL of the content
- **filename**: Original filename
- **title**: Page/content title
- **summary**: Content summary
- **content_type**: Type of content
- **importance_score**: Relevance scoring (1-10)
- **key_points**: Main takeaways

### Link Knowledge Base to Bot
1. In the bot configuration, locate the "Query Search" block
2. Ensure the `knowledgeBaseId` matches your created knowledge base
3. The current configuration searches for top 5 results (`topK: '5'`)

## Step 6: Configure the AI Model

The bot is configured to use:
- **Model**: Gemini 2.5 Flash
- **Temperature**: 0.7 (balanced creativity/consistency)
- **API Key**: References the `GOOGLE_GEMINI_API_KEY` environment variable

Ensure your API key is properly set and accessible to the Sim.ai platform.

## Step 7: Test Your Bot

1. Use the built-in chat interface or preview mode
2. Test with sample queries like:
   - "What is FlexPay?"
   - "How does failed payment recovery work?"
   - "What solutions does FlexPay offer for dating apps?"
   - "Tell me about FlexPay's invisible recovery"

## Bot Behavior

The configured bot will:

1. **Accept user input** through the chat interface
2. **Search the knowledge base** for the 5 most relevant pieces of information
3. **Generate responses** using Gemini 2.5 Flash with this behavior:
   - Provide clear, professional answers
   - Use only verified information from the knowledge base
   - Include direct links when available
   - Format responses with bullet points and headings
   - Avoid speculation or invented details
   - Clearly state when information isn't available

## Troubleshooting

### Common Issues

**Bot not responding:**
- Verify your Gemini API key is correctly set
- Check that the knowledge base is properly linked
- Ensure the YAML file imported successfully

**Poor search results:**
- Review the knowledge base data quality
- Adjust the `topK` value in the Query Search block
- Check that the CSV file uploaded completely

**API errors:**
- Confirm your Gemini API key has sufficient quota
- Verify the API key environment variable name matches exactly
- Check for any API rate limiting

### Environment Variable Verification

To verify your environment variable is set correctly:

**Windows:**
```powershell
echo $env:GOOGLE_GEMINI_API_KEY
```

**Linux/macOS:**
```bash
echo $GOOGLE_GEMINI_API_KEY
```

## Data Overview

Your knowledge base contains **46+ scraped pages** from FlexPay covering:
- Product information and solutions
- Blog content and resources
- Industry-specific applications (dating apps, gaming, SaaS, etc.)
- Payment recovery methodologies
- Company information and policies

The bot can provide information on all these topics based on the scraped content.

## Next Steps

1. Customize the system prompt in the "Summary Agent" block for specific use cases
2. Adjust temperature and other model parameters as needed
3. Add additional knowledge sources if required
4. Set up monitoring and analytics if available in Sim.ai
5. Deploy the bot to your preferred channels (web, Slack, etc.)

## Support

For Sim.ai specific issues, refer to their documentation or support channels. For questions about the FlexPay data or bot configuration, review the source files in your project directory.
