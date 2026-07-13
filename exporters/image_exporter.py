# ==========================================================
# Imports
# ==========================================================

from models.generated_image import GeneratedImage


# ==========================================================
# Image Exporter
# ==========================================================

class ImageExporter:

    @staticmethod
    def export(image: GeneratedImage):

        print("\nImage Exported Successfully")
        print(f"Scene : {image.scene_number}")
        print(f"Saved : {image.image_path}")