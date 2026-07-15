from agents.base_llm_agent import BaseLLMAgent

from models.character_profile import CharacterProfile

from prompts.character.character_prompt import CharacterPrompt

from utils.json_parser import parse_json


class CharacterAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Character Agent")

    def generate_characters(self, research_report):

        return self.run(research_report)

    def run(self, research_report):

        self.start()

        print("Character Generation Started")

        prompt = CharacterPrompt.generate(research_report)

        response = self.think(prompt)

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