from agents.base_llm_agent import BaseLLMAgent

from config.settings import IMAGE_PROMPT_BATCH_SIZE

from prompts.image_prompt_batch import ImagePromptBatchPrompt

from utils.json_parser import parse_json
from utils.image_prompt_mapper import ImagePromptMapper


class ImagePromptAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Image Prompt Agent")

    def generate_image_prompts(
        self,
        scenes,
        character_bibles
    ):

        return self.run(
            scenes,
            character_bibles
        )

    def run(
        self,
        scenes,
        character_bibles
    ):

        self.start()

        print("Image Prompt Generation Started")

        image_prompts = []

        total_scenes = len(scenes)

        for start in range(
            0,
            total_scenes,
            IMAGE_PROMPT_BATCH_SIZE
        ):

            batch = scenes[
                start:start + IMAGE_PROMPT_BATCH_SIZE
            ]

            print(
                f"Generating Image Prompts "
                f"({len(batch)} Scenes)"
            )

            prompt = ImagePromptBatchPrompt.generate(
                batch,
                character_bibles
            )

            response = self.think(prompt)

            data = parse_json(response)

            batch_prompts = ImagePromptMapper.from_json_list(
                data
            )

            image_prompts.extend(
                batch_prompts
            )

        return image_prompts