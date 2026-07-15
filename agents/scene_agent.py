# ==========================================================
# Imports
# ==========================================================

from agents.base_llm_agent import BaseLLMAgent

from prompts.scene_prompt import ScenePrompt

from utils.json_parser import parse_json
from utils.scene_mapper import SceneMapper


# ==========================================================
# Scene Agent
# ==========================================================

class SceneAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Scene Agent")

    def generate_scenes(
        self,
        story,
        character_bibles
    ):

        return self.run(
            story,
            character_bibles
        )

    def run(
        self,
        story,
        character_bibles
    ):

        self.start()

        print("Scene Generation Started")

        prompt = ScenePrompt.generate(
            story,
            character_bibles
        )

        response = self.think(prompt)

        data = parse_json(response)

        scene_list = SceneMapper.from_json(data)

        return scene_list