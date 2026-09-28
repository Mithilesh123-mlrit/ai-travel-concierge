# ✈️ TravelAI — AI Travel Concierge

> An AI-powered travel assistant built with **React, FastAPI, LangGraph, LangChain, Gemini, RAG, and real-world travel APIs**.

**Plan smarter. Travel better. Explore with AI.**

---

## 🌐 Live Demo

### Live Working url
https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app

### API Documentation
https://travelai-backend-wmq4.onrender.com/docs

---

# 📌 Project Overview

TravelAI is an intelligent travel concierge designed to help users plan and explore trips using AI-powered tools and real-world information.

The application combines:

- 🤖 AI Agent
- 🌦️ Weather information
- 🔎 Web search
- 🏨 Hotel search
- 💱 Currency conversion
- 🗺️ AI itinerary generation
- 📄 RAG-based document intelligence
- 📜 Search history
- 🌐 Modern React frontend
- ⚡ FastAPI backend
- 🧠 LangGraph agent workflow

The project was developed as an **8-week Agentic AI project** and upgraded from Track A to the more advanced **Track B architecture**.

---

# 🚀 Features

## 🤖 AI Travel Concierge

Users can ask travel-related questions through a conversational AI interface.

The agent automatically selects the appropriate tool depending on the user's request.

Example:

```text
What is the weather in Hyderabad?
Find hotels in Goa.
Convert 100 USD to INR.
What are the best places to visit in Paris?
🌦️ Weather Information

Uses a weather API to retrieve current weather information for destinations.

Example:

What is the weather in Hyderabad?

The AI agent identifies the request and uses the weather tool.

🔎 Web Search

The travel agent can search the web for current travel information such as:

Tourist attractions
Places to visit
Travel information
Destination information
🏨 Hotel Search

Users can search for accommodation options.

The backend integrates with the StayingAPI to retrieve hotel information.

Example:

Find hotels in Goa.
💱 Currency Conversion

TravelAI provides currency conversion using live exchange-rate data.

Example:

Convert 100 USD to INR.

The currency tool uses the Frankfurter API for exchange-rate information.

🗺️ AI Itinerary Generator

Users can generate personalized travel itineraries based on:

Destination
Number of days
Interests

Example:

Destination: Hyderabad
Days: 3
Interests: Food, history and sightseeing

The AI generates a structured day-by-day itinerary.

📄 RAG Document Intelligence

TravelAI supports document-based question answering.

Users can:

Upload a PDF
Extract the document text
Split the text into chunks
Generate embeddings
Store embeddings in FAISS
Ask questions about the uploaded document

Example:

Upload a travel guide PDF.

Question:
What are the top attractions mentioned in this document?

The system retrieves relevant information from the uploaded document before generating an answer.

📜 Search History

TravelAI stores previous searches using SQLite.

The application can display recent searches through the frontend.

Stored information includes:

Search type
Destination
Check-in date
Check-out date
Number of adults
Query
Timestamp
🧠 Agentic AI Architecture

The project uses LangGraph to create a tool-using AI agent.

                    ┌──────────────────────┐
                    │      React UI        │
                    │      Vite App        │
                    └──────────┬───────────┘
                               │
                               │ HTTP API
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   LangGraph Agent    │
                    │   Travel Concierge   │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼─────────────────┐
              │                │                 │
              ▼                ▼                 ▼
        Weather Tool      Web Search       Hotel Search
              │                │                 │
              └────────────────┼─────────────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
       Currency Tool                     Gemini LLM

The system chooses tools automatically depending on the user's request.

🏗️ Project Architecture
User
 │
 ▼
React + Vite Frontend
 │
 │ REST API
 ▼
FastAPI Backend
 │
 ├── LangGraph Travel Agent
 │     ├── Weather Tool
 │     ├── Web Search Tool
 │     ├── Hotel Search Tool
 │     └── Currency Tool
 │
 ├── Itinerary Service
 │
 ├── RAG Service
 │     ├── PDF Processing
 │     ├── Text Chunking
 │     ├── Gemini Embeddings
 │     └── FAISS Vector Store
 │
 └── SQLite Database
       └── Search History
🛠️ Technology Stack
Frontend
React
Vite
JavaScript
Axios
Lucide React
CSS
Backend
Python
FastAPI
Uvicorn
Pydantic
AI
Google Gemini
LangChain
LangGraph
Gemini Embeddings
RAG
PyPDF
FAISS
Recursive Character Text Splitter
Database
SQLite
APIs
Weather API
Web Search
StayingAPI
Frankfurter Currency API
Deployment
GitHub
Vercel — Frontend
Render — Backend
📂 Project Structure
ai-travel-concierge/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   └── travel_agent.py
│   │   │
│   │   ├── api/
│   │   │
│   │   ├── database/
│   │   │   └── db.py
│   │   │
│   │   ├── rag/
│   │   │   └── rag_service.py
│   │   │
│   │   ├── services/
│   │   │   ├── itinerary.py
│   │   │   └── travel_api.py
│   │   │
│   │   ├── tools/
│   │   │   ├── travel_tools.py
│   │   │   └── currency_tool.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── api.js
│   │   └── main.jsx
│   │
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── README.md
└── LICENSE
⚙️ Local Development Setup
1. Clone the Repository
git clone https://github.com/Mithilesh123-mlrit/ai-travel-concierge.git

Move into the project:

cd ai-travel-concierge
🐍 Backend Setup
2. Create Virtual Environment

Windows:

python -m venv .venv

Activate:

.\.venv\Scripts\Activate.ps1
3. Install Backend Dependencies
pip install -r backend/requirements.txt
4. Configure Environment Variables

Create:

backend/.env

Add:

GEMINI_API_KEY=your_gemini_api_key
STAYING_API_KEY=your_staying_api_key

Never commit .env files or API keys to GitHub.

▶️ Run Backend

From the project root:

uvicorn backend.app.main:app --reload

Backend:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health
⚛️ Frontend Setup

Open another terminal.

Move to:

cd frontend

Install dependencies:

npm install
Frontend Environment Variable

Create:

frontend/.env

For local development:

VITE_API_URL=http://127.0.0.1:8000
▶️ Run Frontend
npm run dev

The frontend will normally be available at:

http://localhost:5173
🔗 Frontend–Backend Communication

The frontend communicates with the FastAPI backend using REST APIs.

Example:

React Frontend
      │
      │ POST /api/travel
      ▼
FastAPI Backend
      │
      ▼
LangGraph Travel Agent
      │
      ├── Weather
      ├── Web Search
      ├── Hotels
      └── Currency
🔌 API Endpoints
Travel Agent
POST /api/travel

Example request:

{
  "question": "What is the weather in Hyderabad?"
}
Search History
GET /api/history
Itinerary
POST /api/itinerary

Example:

{
  "destination": "Goa",
  "days": 3,
  "interests": "beaches, food and sightseeing"
}
RAG Upload
POST /api/rag/upload

Uploads a PDF document for RAG processing.

RAG Question
POST /api/rag/query

Example:

{
  "question": "What are the important places mentioned in the document?"
}
Health Check
GET /health
🧪 Testing

Backend tests are available inside:

backend/tests/

Run tests with:

pytest
🔍 Manual Testing Checklist

After starting both applications, test:

AI Agent
What is the weather in Hyderabad?
Web Search
What are the best places to visit in Paris?
Hotel Search
Find hotels in Goa.
Currency
Convert 100 USD to INR.
Itinerary

Generate a multi-day itinerary.

RAG
Upload a PDF.
Ask a question about its contents.
Search History

Perform searches and verify they appear in Recent Searches.

☁️ Deployment

TravelAI uses two deployment services:

Frontend → Vercel
Backend  → Render
🚀 Backend Deployment — Render

The backend is deployed as a Render Web Service.

Repository
Mithilesh123-mlrit/ai-travel-concierge
Branch
main
Root Directory
.
Build Command
pip install -r backend/requirements.txt
Start Command
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
Health Check
/health
Environment Variables

Add the following in Render:

GEMINI_API_KEY
STAYING_API_KEY

Do not commit these values to GitHub.

⚛️ Frontend Deployment — Vercel

The React frontend is deployed using Vercel.

Repository
Mithilesh123-mlrit/ai-travel-concierge
Root Directory
frontend
Framework
Vite
Build Command
npm run build
Output Directory
dist
Environment Variable
VITE_API_URL=https://travelai-backend-wmq4.onrender.com
🌐 Production URLs
Live Frontend

https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app


FastAPI Documentation

https://travelai-backend-wmq4.onrender.com/docs

🔐 CORS Configuration

The FastAPI backend allows the production Vercel frontend and local development frontend.

Example configuration:

allow_origins=[
    "http://localhost:5173",
    "https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app",
]

This allows the React frontend to communicate with the deployed FastAPI backend.

🔒 Security

API keys are stored using environment variables.

The following files should never be committed:

.env
.env.*

The .gitignore also excludes:

.venv/
__pycache__/
*.pyc
*.db
frontend/node_modules/
frontend/dist/
frontend/.vite/

Never expose API keys in:

Source code
GitHub
Screenshots
README files
Frontend JavaScript
Public repositories
📄 RAG Pipeline

The RAG system follows this workflow:

PDF Upload
    │
    ▼
PDF Text Extraction
    │
    ▼
Text Chunking
    │
    ▼
Gemini Embeddings
    │
    ▼
FAISS Vector Store
    │
    ▼
User Question
    │
    ▼
Similarity Search
    │
    ▼
Relevant Context
    │
    ▼
Gemini LLM
    │
    ▼
Answer

The system uses the uploaded document as the knowledge source for document-related questions.

🤖 Agent Tools

The TravelAI agent has access to multiple tools.

Tool	Purpose
Weather Tool	Current weather information
Web Search Tool	Travel and destination information
Hotel Search Tool	Hotel/accommodation search
Currency Tool	Currency conversion
Itinerary Service	AI-generated travel plans
RAG Service	Document-based question answering

The LangGraph agent determines which tool should be used based on the user's request.

📈 Development Journey
Week 1–2
Created GitHub repository
Set up Python environment
Learned LangChain fundamentals
Built initial AI chatbot
Added document upload
Implemented basic RAG
Deployed initial application
Week 3–4
Added web search
Added weather tool
Implemented tool calling
Added error handling
Tested agent workflows
Week 5–6
Added hotel search
Added SQLite search history
Added itinerary generation
Improved validation
Improved application UI
Week 7–8 — Track B Upgrade
Migrated backend to FastAPI
Introduced LangGraph
Created modular backend architecture
Added currency conversion
Built React + Vite frontend
Added RAG interface
Added search history interface
Created professional dark UI
Added backend API documentation
Deployed backend to Render
Deployed frontend to Vercel
Connected production frontend and backend
Tested production API communication
🏗️ Track B Architecture

The final project follows a more production-oriented architecture:

                    ┌────────────────────┐
                    │    React + Vite    │
                    │     Frontend       │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      FastAPI       │
                    │       Backend      │
                    └─────────┬──────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
       LangGraph          RAG Service      Database
         Agent
             │
      ┌──────┼────────┬──────────┐
      ▼      ▼        ▼          ▼
   Weather  Web     Hotels    Currency
🎯 Project Goals

The project demonstrates practical implementation of:

Generative AI
Agentic AI
LangChain
LangGraph
RAG
API integration
FastAPI
React
SQLite
Cloud deployment
Environment management
Git/GitHub workflow
Production frontend/backend architecture
🔮 Future Improvements

Potential future enhancements include:

✈️ Flight search integration
🏨 More advanced hotel filtering
🗺️ Interactive maps
📍 Location-based recommendations
👤 User authentication
💾 Cloud database
🧠 Long-term conversational memory
📱 Mobile-responsive improvements
📊 User analytics
🔔 Travel alerts
🗓️ Calendar integration
🌍 Multi-language support
👨‍💻 Development

This project was developed as part of an Agentic AI learning and internship project.

The development process focused on learning by building a real-world AI application and progressively moving from a simple AI assistant toward a modular production-style architecture.

📚 Key Learning Outcomes

Through this project, I gained practical experience with:

Building AI agents
Tool calling
LangChain
LangGraph
Retrieval-Augmented Generation
Vector databases
FastAPI
REST APIs
React and Vite
SQLite
API integration
Environment variables
Git and GitHub
Cloud deployment
Frontend/backend communication
Production debugging
📜 License

This project is intended for educational and portfolio purposes.

⭐ Final Project

TravelAI — AI Travel Concierge

Plan smarter. Travel better. Explore with AI.

GitHub

https://github.com/Mithilesh123-mlrit/ai-travel-concierge

Live Application

https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app


API Documentation

https://travelai-backend-wmq4.onrender.com/docs