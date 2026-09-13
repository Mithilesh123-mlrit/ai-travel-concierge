import os
import requests
from dotenv import load_dotenv


load_dotenv()

STAYING_API_KEY = os.getenv("STAYING_API_KEY")


def search_hotels(
    location: str,
    check_in: str,
    check_out: str,
    adults: int = 2
):
    """
    Search hotels for a location and date range.
    """

    if not STAYING_API_KEY:
        return {
            "success": False,
            "error": "Hotel API key is not configured."
        }

    url = "https://api.stayingapi.com/v1/search"

    params = {
        "location": location,
        "checkIn": check_in,
        "checkOut": check_out,
        "adults": adults,
        "platforms": "google",
        "limit": 5
    }

    headers = {
        "Authorization": f"Bearer {STAYING_API_KEY}"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return {
            "success": True,
            "data": data
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Hotel search request timed out."
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": f"Hotel API request failed: {error}"
        }

    except Exception as error:
        return {
            "success": False,
            "error": f"Unexpected error: {error}"
        }