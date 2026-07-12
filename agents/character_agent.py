from agents.base_agent import BaseAgent
from brain.brain import Brain

from models.character_profile import CharacterProfile

from prompts.character.character_prompt import CharacterPrompt

from utils.json_parser import parse_json


class CharacterAgent(BaseAgent):

    def __init__(self):
        super().__init__("Character Agent")

    def generate_characters(self, research_report):

        print("Character Generation Started")

        prompt = CharacterPrompt.generate(research_report)

        brain = Brain()

        response = brain.think(prompt)

        data = parse_json(response)

        characters = []

        for item in data.get("characters", []):

            character = CharacterProfile(
                name=item.get("name", ""),
                role=item.get("role", ""),
                species=item.get("species", ""),
                description=item.get("description", "")
            )

            characters.append(character)

        return characters