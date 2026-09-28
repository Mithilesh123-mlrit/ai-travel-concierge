def generate_itinerary(llm, destination, days, interests="general sightseeing"):
    """
    Generate a simple travel itinerary using the existing LLM.
    """

    if not destination.strip():
        return "Please enter a destination."

    if days < 1:
        return "Number of days must be at least 1."

    prompt = f"""
You are an AI Travel Concierge.

Create a practical {days}-day travel itinerary for {destination}.

Traveler interests:
{interests}

For each day, provide:

Day 1
- Morning
- Afternoon
- Evening

Continue the same format for all {days} days.

Keep the itinerary simple, realistic, and travel-friendly.
Do not invent exact live prices or availability.
"""

    try:
        response = llm.invoke(prompt)

        content = response.content

        # Handle Gemini structured response
        if isinstance(content, list):
            text_parts = []

            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(item.get("text", ""))

            content = "\n".join(text_parts)

        return str(content).strip()

    except Exception:
        return "Unable to generate the itinerary right now. Please try again."