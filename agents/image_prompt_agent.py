from agents.base_agent import BaseAgent
from brain.brain import Brain

from prompts.image_prompt import ImagePromptPrompt

from utils.json_parser import parse_json
from utils.image_prompt_mapper import ImagePromptMapper


class ImagePromptAgent(BaseAgent):

    def __init__(self):
        super().__init__("Image Prompt Agent")

    def generate_image_prompts(
        self,
        scenes,
        character_bibles
    ):

        print("Image Prompt Generation Started")

        brain = Brain()

        image_prompts = []

        for scene in scenes:

            print(
                f"Generating Image Prompt: "
                f"Scene {scene.scene_number}"
            )

            prompt = ImagePromptPrompt.generate(
                scene,
                character_bibles
            )

            response = brain.think(prompt)

            data = parse_json(response)

            image_prompt = ImagePromptMapper.from_json(
                data
            )

            image_prompts.append(
                image_prompt
            )

        return image_prompts