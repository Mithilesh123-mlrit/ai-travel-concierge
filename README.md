✈️ TravelAI — AI Travel Concierge
> An AI-powered travel assistant built with **React, FastAPI, LangGraph, LangChain, Gemini, RAG, and real-world travel APIs**.
Plan smarter. Travel better. Explore with AI.

🌐 Live Demo
Live Application:  
https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app
API Documentation:  
https://travelai-backend-wmq4.onrender.com/docs

📌 Project Overview
TravelAI is an intelligent travel concierge designed to help users plan and explore trips using AI-powered tools and real-world information.
Core Capabilities
🤖 AI Travel Concierge
🌦️ Weather information
🔎 Web search
🏨 Hotel search
💱 Currency conversion
🗺️ AI itinerary generation
📄 RAG-based document intelligence
📜 Search history
🌐 React frontend
⚡ FastAPI backend
🧠 LangGraph agent workflow
The project was developed as an 8-week Agentic AI project and upgraded from Track A to the advanced Track B architecture.

🚀 Features
🤖 AI Travel Concierge
Users can ask travel-related questions through a conversational AI interface. The LangGraph agent automatically selects the appropriate tool based on the user's request.
Examples:
```text

An AI-powered travel assistant built with React, FastAPI, LangGraph, LangChain, Gemini, RAG, and real-world travel APIs.

Plan smarter. Travel better. Explore with AI.

🌐 Live Demo

Live Application:
https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app

API Documentation:
https://travelai-backend-wmq4.onrender.com/docs

📌 Project Overview

TravelAI is an intelligent travel concierge designed to help users plan and explore trips using AI-powered tools and real-world information.

Core Capabilities

🤖 AI Travel Concierge

🌦️ Weather information

🔎 Web search

🏨 Hotel search

💱 Currency conversion

🗺️ AI itinerary generation

📄 RAG-based document intelligence

📜 Search history

🌐 React frontend

⚡ FastAPI backend

🧠 LangGraph agent workflow

The project was developed as an 8-week Agentic AI project and upgraded from Track A to the advanced Track B architecture.

🚀 Features

🤖 AI Travel Concierge

Users can ask travel-related questions through a conversational AI interface. The LangGraph agent automatically selects the appropriate tool based on the user's request.

Examples:

What is the weather in Hyderabad?
Find hotels in Goa.
Convert 100 USD to INR.
What are the best places to visit in Paris?
```
🌦️ Weather Information
Retrieves current weather information for destinations through a weather API.
🔎 Web Search
Searches for current travel information such as:

🌦️ Weather Information

Retrieves current weather information for destinations through a weather API.

🔎 Web Search

Searches for current travel information such as:

Tourist attractions

Places to visit
Destination information
Travel information
🏨 Hotel Search
Searches accommodation options using the StayingAPI.
💱 Currency Conversion
Provides currency conversion using exchange-rate data from the Frankfurter API.

Destination information

Travel information

🏨 Hotel Search

Searches accommodation options using the StayingAPI.

💱 Currency Conversion

Provides currency conversion using exchange-rate data from the Frankfurter API.

Example:
```text
Convert 100 USD to INR.
```
🗺️ AI Itinerary Generator
Generates structured day-by-day travel itineraries based on:

🗺️ AI Itinerary Generator

Generates structured day-by-day travel itineraries based on:

Destination

Number of days

Interests
📄 RAG Document Intelligence
Supports document-based question answering.
Workflow:
Upload a PDF
Extract document text
Split text into chunks

📄 RAG Document Intelligence

Supports document-based question answering.

Workflow:

Upload a PDF

Extract document text

Split text into chunks

Generate embeddings

Store embeddings in FAISS
Ask questions about the document
📜 Search History
Stores previous searches using SQLite and displays recent searches through the frontend.

Ask questions about the document

📜 Search History

Stores previous searches using SQLite and displays recent searches through the frontend.

🧠 Agentic AI Architecture
The project uses LangGraph to create a tool-using AI agent.
```text

React + Vite Frontend
        │
        │ HTTP API
        ▼
FastAPI Backend
        │
        ▼
LangGraph Travel Agent
        │
   ┌────┼───────────────┐
   ▼    ▼       ▼       ▼
Weather Web    Hotels  Currency
 Tool  Search   Tool     Tool
        │
        ▼
    Gemini LLM
```
The agent chooses tools automatically based on the user's request.
🏗️ System Architecture
```text

The agent chooses tools automatically based on the user's request.

🏗️ System Architecture

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
```
🛠️ Technology Stack
Area	Technologies
Frontend	React, Vite, JavaScript, Axios, Lucide React, CSS
Backend	Python, FastAPI, Uvicorn, Pydantic
AI	Google Gemini, LangChain, LangGraph
RAG	Gemini Embeddings, PyPDF, FAISS, Recursive Character Text Splitter
Database	SQLite
APIs	Weather API, Web Search, StayingAPI, Frankfurter Currency API
Deployment	Vercel, Render
Version Control	Git, GitHub

📂 Project Structure
```text

🛠️ Technology Stack

Area

Technologies

Frontend

React, Vite, JavaScript, Axios, Lucide React, CSS

Backend

Python, FastAPI, Uvicorn, Pydantic

AI

Google Gemini, LangChain, LangGraph

RAG

Gemini Embeddings, PyPDF, FAISS, Recursive Character Text Splitter

Database

SQLite

APIs

Weather API, Web Search, StayingAPI, Frankfurter Currency API

Deployment

Vercel, Render

Version Control

Git, GitHub

📂 Project Structure

ai-travel-concierge/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   └── travel_agent.py
│   │   ├── api/
│   │   ├── database/
│   │   │   └── db.py
│   │   ├── rag/
│   │   │   └── rag_service.py
│   │   │   └── database.py
│   │   ├── rag/
│   │   │   └── rag.py
│   │   ├── services/
│   │   │   ├── itinerary.py
│   │   │   └── travel_api.py
│   │   ├── tools/
│   │   │   ├── travel_tools.py
│   │   │   └── currency_tool.py
│   │   │   └── currency.py
│   │   └── main.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── api.js
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── README.md
└── LICENSE
```

⚙️ Local Development Setup

1. Clone the Repository
```bash
git clone https://github.com/Mithilesh123-mlrit/ai-travel-concierge.git
cd ai-travel-concierge
```
2. Backend Setup
Create and activate a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Install dependencies:
```bash
pip install -r backend/requirements.txt
```
Create `backend/.env`:
```env
GEMINI_API_KEY=your_gemini_api_key
STAYING_API_KEY=your_staying_api_key
```
Never commit `.env` files or API keys to GitHub.
Run the backend:
```bash

git clone https://github.com/Mithilesh123-mlrit/ai-travel-concierge.git
cd ai-travel-concierge

2. Backend Setup

Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r backend/requirements.txt

Create backend/.env:

GEMINI_API_KEY=your_gemini_api_key
STAYING_API_KEY=your_staying_api_key

Never commit .env files or API keys to GitHub.

Run the backend:

uvicorn backend.app.main:app --reload
```
Backend:
```text
http://127.0.0.1:8000
```
Swagger documentation:
```text
http://127.0.0.1:8000/docs
```
Health check:
```text
http://127.0.0.1:8000/health
```
3. Frontend Setup
Open another terminal:
```bash
cd frontend
npm install
```
Create `frontend/.env`:
```env
VITE_API_URL=http://127.0.0.1:8000
```
Run the frontend:
```bash
npm run dev
```
Frontend:
```text
http://localhost:5173
```
🔌 API Endpoints
Feature	Method	Endpoint
Travel Agent	POST	`/api/travel`
Search History	GET	`/api/history`
Itinerary	POST	`/api/itinerary`
RAG Upload	POST	`/api/rag/upload`
RAG Question	POST	`/api/rag/query`
Health Check	GET	`/health`
Example travel request:
```json
{
  "question": "What is the weather in Hyderabad?"
}
```
Example itinerary request:
```json

3. Frontend Setup

Open another terminal:

cd frontend
npm install

Create frontend/.env:

VITE_API_URL=http://127.0.0.1:8000

Run the frontend:

npm run dev

Frontend:

http://localhost:5173

🔌 API Endpoints

Feature

Method

Endpoint

Travel Agent

POST

/api/travel

Search History

GET

/api/history

Itinerary

POST

/api/itinerary

RAG Upload

POST

/api/rag/upload

RAG Question

POST

/api/rag/query

Health Check

GET

/health

Example travel request:

{
  "question": "What is the weather in Hyderabad?"
}

Example itinerary request:

{
  "destination": "Goa",
  "days": 3,
  "interests": "beaches, food and sightseeing"
}
```
📄 RAG Pipeline
```text

📄 RAG Pipeline

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
```
The uploaded document is used as the knowledge source for document-related questions.
🧪 Testing
Backend tests are available in:
```text
backend/tests/
```
Run:
```bash
pytest
```
Manual Testing
Test the main capabilities:
```text
=======

The uploaded document is used as the knowledge source for document-related questions.

🧪 Testing

Backend tests are available in:

backend/tests/

Run:

pytest

Manual Testing

Test the main capabilities:

Weather      → What is the weather in Hyderabad?
Web Search   → What are the best places to visit in Paris?
Hotels       → Find hotels in Goa.
Currency     → Convert 100 USD to INR.
Itinerary    → Generate a multi-day itinerary.
RAG          → Upload a PDF and ask a question.
History      → Perform searches and verify Recent Searches.
```
☁️ Deployment
Backend — Render
Repository: `Mithilesh123-mlrit/ai-travel-concierge`
Branch: `main`
Root Directory: `.`
Build Command: `pip install -r backend/requirements.txt`
Start Command: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
Health Check: `/health`
Required environment variables:
```text
GEMINI_API_KEY
STAYING_API_KEY
```
Frontend — Vercel
Repository: `Mithilesh123-mlrit/ai-travel-concierge`
Root Directory: `frontend`
Framework: Vite
Build Command: `npm run build`
Output Directory: `dist`
Production environment variable:
```env
VITE_API_URL=https://travelai-backend-wmq4.onrender.com
```
🌐 Production URLs
Live Application:  
https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app
API Documentation:  
https://travelai-backend-wmq4.onrender.com/docs

🔐 Security
API keys are stored using environment variables.
`.env` files are excluded from Git.
API keys must never be committed to source code.
API keys should not be exposed in screenshots, README files, frontend code, or public repositories.

☁️ Deployment

Backend — Render

Repository: Mithilesh123-mlrit/ai-travel-concierge

Branch: main

Root Directory: .

Build Command: pip install -r backend/requirements.txt

Start Command: uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT

Health Check: /health

Required environment variables:

GEMINI_API_KEY
STAYING_API_KEY

Frontend — Vercel

Repository: Mithilesh123-mlrit/ai-travel-concierge

Root Directory: frontend

Framework: Vite

Build Command: npm run build

Output Directory: dist

Production environment variable:

VITE_API_URL=https://travelai-backend-wmq4.onrender.com

🌐 Production URLs

Live Application:
https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app

API Documentation:
https://travelai-backend-wmq4.onrender.com/docs

🔐 Security

API keys are stored using environment variables.

.env files are excluded from Git.

API keys must never be committed to source code.

API keys should not be exposed in screenshots, README files, frontend code, or public repositories.

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
✈️ Flight search integration
🏨 Advanced hotel filtering


🔮 Future Improvements

✈️ Flight search integration

🏨 Advanced hotel filtering

🗺️ Interactive maps

📍 Location-based recommendations

👤 User authentication

💾 Cloud database

🧠 Long-term conversational memory



📊 User analytics

🔔 Travel alerts

🗓️ Calendar integration

🌍 Multi-language support

📚 Key Learning Outcomes
Through this project, I gained practical experience with:
Building AI agents

Tool calling
LangChain and LangGraph

LangChain and LangGraph

Retrieval-Augmented Generation

Vector databases
FastAPI and REST APIs

FastAPI and REST APIs

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

GitHub:  
https://github.com/Mithilesh123-mlrit/ai-travel-concierge

