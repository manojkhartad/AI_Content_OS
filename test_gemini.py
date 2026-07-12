from google import genai

# Apni actual API key yahan temporarily paste karo
API_KEY = "AQ.Ab8RN6Lqjzrh4BNzUSjdUEZ5ujAQXB04EsJlWZE8ksO_TiWcYA"

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)