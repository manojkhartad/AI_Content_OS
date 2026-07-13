# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
from urllib.parse import quote

import requests


# ==========================================================
# Image Client
# ==========================================================

class ImageClient:

    BASE_URL = "https://image.pollinations.ai/prompt/"


    @staticmethod
    def generate_image(
        prompt: str,
        output_path: Path,
        width: int = 1024,
        height: int = 576,
    ) -> Path:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        encoded_prompt = quote(prompt)

        image_url = (
            f"{ImageClient.BASE_URL}"
            f"{encoded_prompt}"
            f"?width={width}"
            f"&height={height}"
            f"&model=flux"
        )

        print("\nGenerating Image...")
        print(image_url)

        response = requests.get(
            image_url,
            timeout=180
        )

        response.raise_for_status()

        with open(output_path, "wb") as file:
            file.write(response.content)

        print(f"Image Saved : {output_path}")

        return output_path