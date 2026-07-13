import json
from dataclasses import asdict

from config.paths import IMAGE_PROMPTS_DIR


class ImagePromptExporter:

    @staticmethod
    def export(image_prompts):

        for image_prompt in image_prompts:

            filename = (
                f"scene_"
                f"{image_prompt.scene_number:03d}.json"
            )

            filepath = IMAGE_PROMPTS_DIR / filename

            with open(
                filepath,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    asdict(image_prompt),
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        print("\nImage Prompts exported successfully.")
        print(IMAGE_PROMPTS_DIR)