from services.travel_api import search_hotels


print("----- HOTEL SEARCH TEST -----")

result = search_hotels(
    location="Goa, India",
    check_in="2026-10-10",
    check_out="2026-10-12",
    adults=2
)

if result["success"]:
    print("Hotel API working!")
    print(result["data"])
else:
    print("Error:")
    print(result["error"])