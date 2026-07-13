from dataclasses import dataclass


@dataclass
class GeneratedImage:

    scene_id: str

    scene_number: int

    title: str

    prompt: str

    image_path: str

    width: int

    height: int

    provider: str

    model: str