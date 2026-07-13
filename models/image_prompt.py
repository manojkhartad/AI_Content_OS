from dataclasses import dataclass


@dataclass
class ImagePrompt:

    scene_id: str

    scene_number: int

    title: str

    positive_prompt: str

    negative_prompt: str

    style: str

    aspect_ratio: str

    image_size: str