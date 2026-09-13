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
- Hotel search API integration
- LangChain tool calling
- Automatic tool selection
- Basic error handling
- Tool testing scripts
- Agent testing
- Streamlit agent integration
- SQLite-based search history
- Automatic saving of user travel queries
- AI-based itinerary generation

## Agent Capabilities

The agent automatically selects the appropriate tool based on the user's request.

### Example 1

**User:** What is the current weather in Hyderabad?

**Agent:** Uses the Weather API tool.

### Example 2

**User:** Find tourist attractions in Goa.

**Agent:** Uses the Web Search tool.

### Example 3

**User:** Find hotels in Goa from 2026-10-10 to 2026-10-12 for 2 adults.

**Agent:** Uses the Hotel Search tool.

### Itinerary Generation

Users can generate a basic travel itinerary by providing:

- Destination
- Number of days
- Travel interests

The AI generates a day-by-day travel plan with morning, afternoon, and evening activities.

### Search History

The application uses SQLite to store user travel queries and maintain basic search history.

