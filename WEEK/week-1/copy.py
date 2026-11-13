
import os
from dotenv import load_dotenv
from google import genai

print("Starting Gemini program...")

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Connecting to Google Gemini...")

try:
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents="What is Artificial Intelligence? Explain in simple words."
    )

    print("\nGemini Response:")
    print(response.text)

except Exception as e:
    print("\nError occurred:")
    print(e)
