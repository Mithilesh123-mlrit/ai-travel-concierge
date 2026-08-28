import os

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.agents import create_agent
from tools.travel_tools import get_weather, web_search

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

# --------------------------------------------------
# Streamlit page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Travel Concierge",
    page_icon="✈️"
)


# --------------------------------------------------
# Application title
# --------------------------------------------------

st.title("✈️ AI Travel Concierge")
st.write("Ask me a travel-related question.")


# --------------------------------------------------
# Check Gemini API key
# --------------------------------------------------

if not api_key:
    st.error("Gemini API key is not configured.")
    st.stop()


# --------------------------------------------------
# Initialize Gemini LLM
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

# --------------------------------------------------
# Travel Agent
# --------------------------------------------------

tools = [
    get_weather,
    web_search
]

travel_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are an AI Travel Concierge.

Use get_weather when the user asks about current
weather or temperature for a city.

Use web_search when the user asks for current
travel information, tourist attractions, or places to visit.

Choose the appropriate tool automatically.

If a tool cannot find information, explain the problem
clearly instead of inventing an answer.
"""
)

# --------------------------------------------------
# Document Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a travel PDF",
    type=["pdf"]
)

document_text = ""


# --------------------------------------------------
# PDF Text Extraction
# --------------------------------------------------

if uploaded_file is not None:

    try:

        reader = PdfReader(uploaded_file)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                document_text += text + "\n"


        st.success("PDF uploaded and processed successfully!")


        # Preview extracted PDF text
        with st.expander("Preview extracted text"):

            st.write(document_text[:3000])


    except Exception as error:

        st.error(
            f"Error while reading PDF: {error}"
        )


# --------------------------------------------------
# Text Chunking
# --------------------------------------------------

chunks = []

if document_text:

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(
        document_text
    )


    st.success(
        f"Document split into {len(chunks)} chunks."
    )


    # Preview first chunk
    with st.expander("Preview first chunk"):

        if chunks:

            st.write(
                chunks[0]
            )

# --------------------------------------------------
# Embeddings + Vector Store
# --------------------------------------------------

vector_store = None

if chunks:

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    try:

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )

        st.success("Embeddings created and stored in vector database.")

    except Exception as error:

        st.error(
            f"Error while creating embeddings: {error}"
        )

# --------------------------------------------------
# User Question
# --------------------------------------------------

user_input = st.text_input(
    "Ask a question based on the uploaded travel PDF:"
)


# --------------------------------------------------
# Retrieval + RAG Response
# --------------------------------------------------

if st.button("Ask"):

    if not user_input.strip():

        st.warning("Please enter a question.")

    elif vector_store is None:

        st.warning("Please upload a travel PDF first.")

    else:

        try:

            with st.spinner("Searching document and generating answer..."):

                # Retrieve relevant chunks
                relevant_docs = vector_store.similarity_search(
                    user_input,
                    k=3
                )

                # Combine retrieved text
                context = "\n\n".join(
                    doc.page_content
                    for doc in relevant_docs
                )

                # RAG prompt
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
{user_input}

Answer:
"""

                # Generate response using Gemini
                response = llm.invoke(prompt)

            st.subheader("🤖 AI Response")

            st.write(response.content)

            # Show retrieved chunks
            with st.expander("View retrieved document context"):

                for index, doc in enumerate(
                    relevant_docs,
                    start=1
                ):
                    st.write(f"### Retrieved Chunk {index}")
                    st.write(doc.page_content)

        except Exception as error:

            st.error(
                f"Something went wrong: {error}"
            )

# --------------------------------------------------
# Live Travel Agent
# --------------------------------------------------

st.divider()

st.subheader("🌍 Live Travel Assistant")

st.write(
    "Ask about current weather or search for "
    "travel information from the web."
)

agent_question = st.text_input(
    "Ask the Travel Agent:",
    placeholder="Example: What is the weather in Goa?",
    key="agent_question"
)

if st.button(
    "Ask Travel Agent",
    key="agent_button"
):

    if not agent_question.strip():

        st.warning(
            "Please enter a travel-related question."
        )

    else:

        try:

            with st.spinner(
                "Travel Agent is working..."
            ):

                result = travel_agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": agent_question
                            }
                        ]
                    }
                )

                response_content = (
                    result["messages"][-1].content
                )

            # Handle Gemini structured responses
            if isinstance(response_content, list):

                answer_text = ""

                for item in response_content:

                    if (
                        isinstance(item, dict)
                        and item.get("type") == "text"
                    ):

                        answer_text += item.get(
                            "text",
                            ""
                        )

            else:

                answer_text = response_content

            st.subheader("🤖 Agent Response")

            st.write(answer_text)

        except Exception:

            st.error(
                "The Travel Agent could not complete "
                "the request. Please try again."
            )
