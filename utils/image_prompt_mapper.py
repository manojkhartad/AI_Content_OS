from models.image_prompt import ImagePrompt


class ImagePromptMapper:

    @staticmethod
    def from_json(data):

        return ImagePrompt(

            scene_id=data.get(
                "scene_id",
                ""
            ),

            scene_number=data.get(
                "scene_number",
                0
            ),

            title=data.get(
                "title",
                ""
            ),

            positive_prompt=data.get(
                "positive_prompt",
                ""
            ),

            negative_prompt=data.get(
                "negative_prompt",
                ""
            ),

            style=data.get(
                "style",
                "Pixar 3D Animated Movie"
            ),

            aspect_ratio=data.get(
                "aspect_ratio",
                "16:9"
            ),

            image_size=data.get(
                "image_size",
                "1024x576"
            )

        )