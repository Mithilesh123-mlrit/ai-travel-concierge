# AI Travel Concierge

AI-powered Travel Concierge built using LLMs, LangChain, RAG, and Streamlit.

## Live Demo

[AI Travel Concierge](https://ai-travel-concierge-bqkyolvmcztpccgrfybfjn.streamlit.app/)

## Core Features

- PDF document upload
- PDF text extraction
- Text chunking
- Gemini embeddings
- FAISS vector database
- RAG-based document question answering
- Streamlit interface

## Agent Features

- Weather API integration
- Web search integration
- LangChain tool calling
- Automatic tool selection
- Basic error handling
- Tool testing scripts
- Agent testing
- Streamlit agent integration

## Agent Capabilities

The agent automatically selects the appropriate tool based on the user's request.

### Example 1

**User:** What is the current weather in Hyderabad?

**Agent:** Uses the Weather API tool.

### Example 2

**User:** Find tourist attractions in Goa.

**Agent:** Uses the Web Search tool.