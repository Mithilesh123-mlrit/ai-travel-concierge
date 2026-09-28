from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from backend.app.rag.rag_service import (
    process_pdf,
    ask_rag_question,
)
from backend.app.database.db import (
    create_tables,
    save_search,
    get_search_history,
)
from backend.app.services.itinerary import generate_itinerary
from backend.app.agents.travel_agent import travel_agent, llm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Travel Concierge API",
    description="Backend API for the AI Travel Concierge",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://ai-travel-concierge-2j9wi1e9h-ai-travel4.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
create_tables()


class TravelQuery(BaseModel):
    question: str
class ItineraryRequest(BaseModel):
    destination: str
    days: int
    interests: str = "general sightseeing"
class RAGQuestion(BaseModel):
    question: str
rag_vector_store = None


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AI Travel Concierge API",
    }


@app.post("/api/travel")
def travel_query(query: TravelQuery):
    result = travel_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query.question,
                }
            ]
        }
    )

    messages = result.get("messages", [])

    if not messages:
        return {
            "success": False,
            "answer": "No response was generated.",
        }

    answer = messages[-1].content

    if isinstance(answer, list):
        answer = "\n".join(
            block.get("text", "")
            for block in answer
            if isinstance(block, dict) and block.get("text")
        )
    save_search(
    search_type="agent_query",
    query=query.question,
)

    return {
        "success": True,
        "answer": answer,
    }
@app.post("/api/rag/upload")
async def upload_document(file: UploadFile = File(...)):
    global rag_vector_store

    if not file.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "message": "Only PDF files are supported.",
        }

    try:
        file_bytes = await file.read()

        result = process_pdf(file_bytes)

        rag_vector_store = result["vector_store"]

        return {
            "success": True,
            "filename": file.filename,
            "chunks": len(result["chunks"]),
            "message": "PDF uploaded and processed successfully.",
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"Error processing PDF: {error}",
        }


@app.post("/api/rag/query")
def rag_query(query: RAGQuestion):
    if rag_vector_store is None:
        return {
            "success": False,
            "answer": "Please upload a travel PDF first.",
        }

    try:
        result = ask_rag_question(
            rag_vector_store,
            query.question,
        )

        return {
            "success": True,
            "answer": result["answer"],
            "sources": result["sources"],
        }

    except Exception as error:
        return {
            "success": False,
            "answer": f"Something went wrong: {error}",
        }
@app.get("/api/history")
def search_history():
    try:
        rows = get_search_history()

        history = [
            {
                "id": row[0],
                "search_type": row[1],
                "destination": row[2],
                "check_in": row[3],
                "check_out": row[4],
                "adults": row[5],
                "query": row[6],
                "created_at": row[7],
            }
            for row in rows
        ]

        return {
            "success": True,
            "history": history,
        }

    except Exception as error:
        return {
            "success": False,
            "history": [],
            "message": f"Could not load search history: {error}",
        }
@app.post("/api/itinerary")
def create_itinerary(request: ItineraryRequest):
    if not request.destination.strip():
        return {
            "success": False,
            "message": "Destination cannot be empty.",
        }

    if request.days < 1 or request.days > 30:
        return {
            "success": False,
            "message": "Days must be between 1 and 30.",
        }

    try:
        itinerary = generate_itinerary(
            llm=llm,
            destination=request.destination,
            days=request.days,
            interests=request.interests,
        )

        return {
            "success": True,
            "destination": request.destination,
            "days": request.days,
            "itinerary": itinerary,
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"Could not generate itinerary: {error}",
        }