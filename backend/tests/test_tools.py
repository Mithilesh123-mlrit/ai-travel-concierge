from tools.travel_tools import get_weather, web_search


# --------------------------------------------------
# Test 1: Valid Weather
# --------------------------------------------------

print("\n----- TEST 1: VALID WEATHER -----")

weather_result = get_weather.invoke(
    {"city": "Hyderabad"}
)

print(weather_result)


# --------------------------------------------------
# Test 2: Invalid City
# --------------------------------------------------

print("\n----- TEST 2: INVALID WEATHER CITY -----")

invalid_weather_result = get_weather.invoke(
    {"city": "asdfghjkl"}
)

print(invalid_weather_result)


# --------------------------------------------------
# Test 3: Normal Web Search
# --------------------------------------------------

print("\n----- TEST 3: NORMAL WEB SEARCH -----")

search_result = web_search.invoke(
    {
        "query": "best tourist places to visit in Hyderabad"
    }
)

print(search_result)


# --------------------------------------------------
# Test 4: Unusual / No Useful Search
# --------------------------------------------------

print("\n----- TEST 4: UNUSUAL WEB SEARCH -----")

unusual_search_result = web_search.invoke(
    {
        "query": "xyzabc123randomplace travel information"
    }
)

print(unusual_search_result)