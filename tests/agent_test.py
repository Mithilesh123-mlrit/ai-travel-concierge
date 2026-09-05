import os

from dotenv import load_dotenv
from langchain.agents import create_agent

from tools.travel_tools import get_weather, web_search


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# --------------------------------------------------
# Create Agent
# --------------------------------------------------

tools = [
    get_weather,
    web_search
]

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=tools,
    system_prompt="""
You are an AI Travel Concierge.

Use get_weather when the user asks about current
weather or temperature.

Use web_search when the user asks about tourist
attractions, places to visit, or current travel information.

Choose the correct tool automatically.

If the required information cannot be found,
give a clear and friendly response.
"""
)


def run_test(title, question):

    print(f"\n----- {title} -----")
    print(f"Question: {question}")

    try:

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            }
        )

        print(
            "Response:",
            result["messages"][-1].content
        )

    except Exception as error:

        print(
            "Friendly Error:",
            error
        )


# --------------------------------------------------
# Test 1: Weather Tool
# --------------------------------------------------

run_test(
    "TEST 1: WEATHER TOOL SELECTION",
    "What is the current weather in Hyderabad?"
)


# --------------------------------------------------
# Test 2: Web Search Tool
# --------------------------------------------------

run_test(
    "TEST 2: WEB SEARCH TOOL SELECTION",
    "Find tourist attractions to visit in Goa."
)


# --------------------------------------------------
# Test 3: Invalid City
# --------------------------------------------------

run_test(
    "TEST 3: INVALID CITY",
    "What is the weather in asdfghjkl?"
)


# --------------------------------------------------
# Test 4: Unusual Search
# --------------------------------------------------

run_test(
    "TEST 4: UNUSUAL SEARCH",
    "Find travel information about xyzabc123randomplace."
)


# --------------------------------------------------
# Test 5: Empty Question
# --------------------------------------------------

run_test(
    "TEST 5: EMPTY QUESTION",
    ""
)