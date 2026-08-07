from google import genai
from google.genai import types
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_billing_response(customer_name: str, total_debt: float):
    system_instruction = (
        "Du bist ein KI-Assistent für ein deutsches Energieunternehmen. "
        "Deine Aufgabe ist es, Kunden höflich über ihre Schulden zu informieren. "
        "Antworte immer auf Deutsch! "
        "Wenn der Kunde Schulden hat, erinnere ihn höflich daran, diese zu bezahlen. "
    )

    user_message = f"Kunde: {customer_name}. Aktuelle Schulden: {total_debt} Euro. Schreibe eine Antwort an ihn."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
        ),
    )
    return response.text