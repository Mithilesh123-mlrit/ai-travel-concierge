import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from backend.app.tools.currency import convert_currency
from backend.app.tools.travel_tools import (
    get_weather,
    web_search,
    hotel_search,
)


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


# --------------------------------------------------
# Travel Agent Tools
# --------------------------------------------------

tools = [
    get_weather,
    web_search,
    hotel_search,
    convert_currency,
]


# --------------------------------------------------
# LangGraph Travel Agent
# --------------------------------------------------

travel_agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="""
You are an AI Travel Concierge.

Use get_weather when the user asks about current
weather or temperature for a city.

Use web_search when the user asks for current
travel information, tourist attractions, or places to visit.

Use hotel_search when the user asks to find hotels
or accommodation for a destination.

Choose the appropriate tool automatically.

If a tool cannot find information, explain the problem
clearly instead of inventing an answer.

Use convert_currency when the user asks to convert
money between currencies or asks about exchange rates.

Examples:
- "Convert 100 USD to INR"
- "How much is 5000 INR in USD?"
- "What is the current USD to EUR exchange rate?"
""",
)