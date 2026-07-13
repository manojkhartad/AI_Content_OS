# ==========================================================
# Imports
# ==========================================================

from agents.base_agent import BaseAgent
from brain.brain import Brain

from prompts.scene_prompt import ScenePrompt

from utils.json_parser import parse_json
from utils.scene_mapper import SceneMapper


# ==========================================================
# Scene Agent
# ==========================================================

class SceneAgent(BaseAgent):

    def __init__(self):
        super().__init__("Scene Agent")

    def generate_scenes(
        self,
        story,
        character_bibles
    ):

        print("Scene Generation Started")

        prompt = ScenePrompt.generate(
            story,
            character_bibles
        )

        brain = Brain()

        response = brain.think(prompt)

        data = parse_json(response)

        scene_list = SceneMapper.from_json(data)

        return scene_list