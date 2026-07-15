# ==========================================================
# Imports
# ==========================================================

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)

from agents.base_agent import BaseAgent
from brain.image_client import ImageClient
from config.paths import IMAGES_DIR
from config.settings import (
    IMAGE_GENERATION_WORKERS,
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    IMAGE_PROVIDER,
    IMAGE_MODEL,
)
from exporters.image_exporter import ImageExporter
from models.generated_image import GeneratedImage


# ==========================================================
# Image Generation Agent
# ==========================================================

class ImageGenerationAgent(BaseAgent):

    def __init__(self):

        super().__init__("Image Generation Agent")

    def generate_images(self, image_prompts):

        return self.run(image_prompts)

    # ------------------------------------------------------
    # Generate Single Image
    # ------------------------------------------------------

    def _generate_single_image(self, prompt):

        print(
            f"\nGenerating Image : Scene {prompt.scene_number}"
        )

        filename = (
            f"scene_{prompt.scene_number:03d}.png"
        )

        output_path = IMAGES_DIR / filename

        # --------------------------------------------------
        # Resume Support
        # --------------------------------------------------

        if output_path.exists():

            print(
                f"\n✓ Image Already Exists : Scene {prompt.scene_number}"
            )

            return GeneratedImage(

                scene_id=prompt.scene_id,

                scene_number=prompt.scene_number,

                title=prompt.title,

                prompt=prompt.positive_prompt,

                image_path=str(output_path),

                width=IMAGE_WIDTH,

                height=IMAGE_HEIGHT,

                provider=IMAGE_PROVIDER,

                model=IMAGE_MODEL,

            )

        # --------------------------------------------------
        # Generate Image
        # --------------------------------------------------

        ImageClient.generate_image(

            prompt=prompt.positive_prompt,

            output_path=output_path

        )

        image = GeneratedImage(

            scene_id=prompt.scene_id,

            scene_number=prompt.scene_number,

            title=prompt.title,

            prompt=prompt.positive_prompt,

            image_path=str(output_path),

            width=IMAGE_WIDTH,

            height=IMAGE_HEIGHT,

            provider=IMAGE_PROVIDER,

            model=IMAGE_MODEL,

        )

        ImageExporter.export(image)

        print("\nImage Exported Successfully")

        print(
            f"Scene : {prompt.scene_number}"
        )

        print(
            f"Saved : {output_path}"
        )

        return image

    # ------------------------------------------------------
    # Run
    # ------------------------------------------------------

    def run(self, image_prompts):

        self.start()

        print("Image Generation Started")

        generated_images = []

        failed_prompts = []

        # --------------------------------------------------
        # First Pass (Parallel)
        # --------------------------------------------------

        with ThreadPoolExecutor(

            max_workers=IMAGE_GENERATION_WORKERS

        ) as executor:

            future_map = {

                executor.submit(

                    self._generate_single_image,

                    prompt

                ): prompt

                for prompt in image_prompts

            }

            for future in as_completed(future_map):

                prompt = future_map[future]

                try:

                    image = future.result()

                    generated_images.append(image)

                except Exception as e:

                    print(
                        f"\n❌ Failed Scene {prompt.scene_number}"
                    )

                    print(e)

                    failed_prompts.append(prompt)

        # --------------------------------------------------
        # Retry Failed Images
        # --------------------------------------------------

        if failed_prompts:

            print("\n===================================")
            print("Retrying Failed Images...")
            print("===================================")

        retry_failed = []

        for prompt in failed_prompts:

            try:

                image = self._generate_single_image(
                    prompt
                )

                generated_images.append(image)

            except Exception as e:

                print(
                    f"\n❌ Retry Failed : Scene {prompt.scene_number}"
                )

                print(e)

                retry_failed.append(prompt)

        # --------------------------------------------------
        # Sort
        # --------------------------------------------------

        generated_images.sort(

            key=lambda image: image.scene_number

        )

        # --------------------------------------------------
        # Summary
        # --------------------------------------------------

        print("\n===================================")
        print("Image Generation Summary")
        print("===================================")

        print(
            f"Total Images : {len(image_prompts)}"
        )

        print(
            f"Generated    : {len(generated_images)}"
        )

        print(
            f"Failed       : {len(retry_failed)}"
        )

        if retry_failed:

            print("\nFailed Scenes")

            for prompt in retry_failed:

                print(
                    f"Scene {prompt.scene_number}"
                )

        print("===================================")

        return generated_images
    