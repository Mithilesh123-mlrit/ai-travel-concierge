import requests
from langchain_core.tools import tool
from ddgs import DDGS


@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    """

    try:
        # Get latitude and longitude
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"Could not find the city: {city}"

        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data.get("current", {})

        temperature = current.get("temperature_2m")
        wind_speed = current.get("wind_speed_10m")

        return (
            f"Current weather in {city}: "
            f"Temperature: {temperature}°C, "
            f"Wind Speed: {wind_speed} km/h."
        )

    except requests.RequestException:
        return "Weather service is currently unavailable."

    except Exception as error:
        return f"Unable to get weather information: {error}"
@tool
def web_search(query: str) -> str:
    """
    Search the web for current travel-related information.
    """

    try:
        results = DDGS().text(
            query,
            max_results=5
        )

        if not results:
            return "No web search results were found."

        formatted_results = []

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")
            url = result.get("href", "")

            formatted_results.append(
                f"Title: {title}\n"
                f"Summary: {body}\n"
                f"URL: {url}"
            )

        return "\n\n".join(formatted_results)

    except Exception as error:
        return f"Web search is currently unavailable: {error}"