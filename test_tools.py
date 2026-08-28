from tools.travel_tools import get_weather, web_search


print("----- WEATHER TOOL -----")

weather_result = get_weather.invoke(
    {"city": "Hyderabad"}
)

print(weather_result)


print("\n----- WEB SEARCH TOOL -----")

search_result = web_search.invoke(
    {
        "query": "best tourist places to visit in Hyderabad"
    }
)

print(search_result)