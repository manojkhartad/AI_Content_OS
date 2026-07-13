from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemma-4-31b-it",
    contents="Say hello in one sentence."
)

print(response.text)