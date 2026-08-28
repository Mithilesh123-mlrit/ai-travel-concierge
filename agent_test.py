import os

from dotenv import load_dotenv
from langchain.agents import create_agent

from tools.travel_tools import get_weather, web_search


# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# Create tool list
tools = [
    get_weather,
    web_search
]


# Create AI agent
agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=tools,
    system_prompt="""
You are an AI Travel Concierge.

Use the weather tool when the user asks about
current weather or temperature for a city.

Use the web search tool when the user asks for
current travel information, tourist attractions,
places to visit, or information from the web.

Choose the correct tool automatically.
Give clear and concise travel-related answers.
"""
)


# --------------------------------------------------
# Test Weather Tool Selection
# --------------------------------------------------

print("\n----- TEST 1: WEATHER -----")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the current weather in Hyderabad?"
            }
        ]
    }
)

print(result["messages"][-1].content)


# --------------------------------------------------
# Test Web Search Tool Selection
# --------------------------------------------------

print("\n----- TEST 2: WEB SEARCH -----")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Find some current tourist attractions in Hyderabad."
            }
        ]
    }
)

print(result["messages"][-1].content)

print("\n----- TEST 3: INVALID CITY -----")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the weather in asdfghjkl?"
            }
        ]
    }
)

print(result["messages"][-1].content)

print("\n----- TEST 4: EMPTY QUERY -----")

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": ""
                }
            ]
        }
    )

    print(result["messages"][-1].content)

except Exception as error:
    print("Please enter a valid question.")

    print("\n----- TEST 5: NO USEFUL SEARCH RESULT -----")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Find tourist information about xyzabc123randomplace"
            }
        ]
    }
)

print(result["messages"][-1].content)

