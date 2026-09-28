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

    if not location or not location.strip():
        return {
            "success": False,
            "error": "Please enter a valid destination."
        }

    if not check_in or not check_out:
        return {
            "success": False,
            "error": "Check-in and check-out dates are required."
        }

    if adults < 1:
        return {
            "success": False,
            "error": "Number of adults must be at least 1."
        }

    url = "https://api.stayingapi.com/v1/search"

    params = {
        "location": location.strip(),
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

        if response.status_code == 401:
            return {
                "success": False,
                "error": "Hotel API authentication failed."
            }

        if response.status_code == 429:
            return {
                "success": False,
                "error": "Hotel API request limit reached. Please try again later."
            }

        if response.status_code >= 500:
            return {
                "success": False,
                "error": "Hotel service is temporarily unavailable."
            }

        response.raise_for_status()

        data = response.json()

        if not data:
            return {
                "success": False,
                "error": "No hotel results were found."
            }

        return {
            "success": True,
            "data": data
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Hotel search timed out. Please try again."
        }

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "Could not connect to the hotel service."
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": f"Hotel search failed: {error}"
        }

    except ValueError:
        return {
            "success": False,
            "error": "Invalid response received from the hotel service."
        }

    except Exception:
        return {
            "success": False,
            "error": "An unexpected hotel search error occurred."
        }