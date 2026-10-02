import requests
from langchain_core.tools import tool


@tool
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
) -> str:
    """Convert an amount from one currency to another using current exchange rates."""

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if amount < 0:
        return "Amount cannot be negative."

    if from_currency == to_currency:
        return f"{amount:.2f} {from_currency} = {amount:.2f} {to_currency}"

    url = (
        f"https://api.frankfurter.dev/v2/rate/"
        f"{from_currency}/{to_currency}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        rate = data["rate"]

        converted_amount = amount * rate

        return (
            f"{amount:.2f} {from_currency} = "
            f"{converted_amount:.2f} {to_currency} "
            f"(rate: {rate:.6f})"
        )

    except requests.RequestException:
        return "Unable to retrieve the current exchange rate."

    except (KeyError, TypeError, ValueError):
        return "Invalid currency or exchange-rate response."