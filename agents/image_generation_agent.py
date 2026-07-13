# ==========================================================
# Imports
# ==========================================================

from agents.base_agent import BaseAgent
from brain.image_client import ImageClient
from config.paths import IMAGES_DIR
from exporters.image_exporter import ImageExporter
from models.generated_image import GeneratedImage


# ==========================================================
# Image Generation Agent
# ==========================================================

class ImageGenerationAgent(BaseAgent):

    def __init__(self):
        super().__init__("Image Generation Agent")

    def generate_images(self, image_prompts):

        print("Image Generation Started")

        generated_images = []

        for prompt in image_prompts:

            print(
                f"\nGenerating Image : Scene {prompt.scene_number}"
            )

            filename = (
                f"scene_{prompt.scene_number:03d}.png"
            )

            output_path = IMAGES_DIR / filename

            try:

                ImageClient.generate_image(
                    prompt=prompt.positive_prompt,
                    output_path=output_path
                )

            except Exception as e:

                print(
                    f"\n❌ Failed Scene {prompt.scene_number}"
                )
                print(e)

                continue

            image = GeneratedImage(
                scene_id=prompt.scene_id,
                scene_number=prompt.scene_number,
                title=prompt.title,
                prompt=prompt.positive_prompt,
                image_path=str(output_path),
                width=1024,
                height=576,
                provider="Pollinations",
                model="flux"
            )

            ImageExporter.export(image)

            generated_images.append(image)

        return generated_images