from pathlib import Path

from google import genai
from dotenv import load_dotenv

from config.settings import GEMINI_API_KEY


# ============================================
# Load Environment Variables
# ============================================

load_dotenv()


# ============================================
# Output Folder
# ============================================

output_dir = Path("production/images")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "test_image.png"


# ============================================
# Prompt
# ============================================

prompt = """
A cute baby lion wearing a tiny red royal cape,
Pixar-style 3D animation,
cinematic lighting,
highly detailed,
vibrant colors,
16:9,
8K quality
"""


# ============================================
# Gemini Client
# ============================================

client = genai.Client(api_key=GEMINI_API_KEY)


# ============================================
# Generate Image
# ============================================

print("Generating image...")

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
)


# ============================================
# Save Image
# ============================================

image_found = False

for part in response.parts:

    if part.text is not None:
        print(part.text)

    elif part.inline_data is not None:

        image = part.as_image()

        image.save(output_file)

        image_found = True

        print("\nImage saved successfully.")
        print(output_file)


if not image_found:

    print("\nNo image returned by Gemini.")