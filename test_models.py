from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

print("Testing models...\n")

for model in client.models.list():
    name = model.name

    try:
        response = client.models.generate_content(
            model=name,
            contents="Reply with only the word: OK"
        )

        print(f"✅ WORKS: {name}")
        print("Response:", response.text)
        print("-" * 50)

    except Exception as e:
        print(f"❌ FAIL: {name}")
        print(type(e).__name__)