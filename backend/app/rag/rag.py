import os
from io import BytesIO

from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured.")


# --------------------------------------------------
# Initialize Gemini
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key,
)


# --------------------------------------------------
# Extract PDF text
# --------------------------------------------------

def extract_pdf_text(file_bytes: bytes) -> str:
    """
    Extract text from an uploaded PDF.
    """

    reader = PdfReader(BytesIO(file_bytes))

    document_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            document_text += text + "\n"

    if not document_text.strip():
        raise ValueError("The uploaded PDF does not contain readable text.")

    return document_text


# --------------------------------------------------
# Split document into chunks
# --------------------------------------------------

def split_document(document_text: str) -> list[str]:
    """
    Split extracted document text into overlapping chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = text_splitter.split_text(document_text)

    if not chunks:
        raise ValueError("No text chunks could be created from the document.")

    return chunks


# --------------------------------------------------
# Create FAISS vector store
# --------------------------------------------------

def create_vector_store(chunks: list[str]) -> FAISS:
    """
    Create a FAISS vector store from document chunks.
    """

    return FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
    )


# --------------------------------------------------
# Ask question using RAG
# --------------------------------------------------

def ask_rag_question(
    vector_store: FAISS,
    question: str,
    k: int = 3,
) -> dict:
    """
    Retrieve relevant document chunks and generate
    an answer using Gemini.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    relevant_docs = vector_store.similarity_search(
        question,
        k=k,
    )

    if not relevant_docs:
        return {
            "answer": (
                "The uploaded document does not contain enough "
                "information to answer this question."
            ),
            "sources": [],
        }

    context = "\n\n".join(
        doc.page_content
        for doc in relevant_docs
    )

    prompt = f"""
You are an AI Travel Concierge.

Answer the user's question using only the information
provided in the uploaded travel document.

If the answer is not available in the document,
say: "The uploaded document does not contain enough
information to answer this question."

Document Context:
{context}

User Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    answer = response.content

    if isinstance(answer, list):
        answer = "\n".join(
            block.get("text", "")
            for block in answer
            if isinstance(block, dict) and block.get("text")
        )

    return {
        "answer": answer,
        "sources": [
            doc.page_content
            for doc in relevant_docs
        ],
    }


# --------------------------------------------------
# Complete document processing helper
# --------------------------------------------------

def process_pdf(file_bytes: bytes) -> dict:
    """
    Extract, split, and vectorize an uploaded PDF.
    """

    document_text = extract_pdf_text(file_bytes)

    chunks = split_document(document_text)

    vector_store = create_vector_store(chunks)

    return {
        "document_text": document_text,
        "chunks": chunks,
        "vector_store": vector_store,
    }