from agents.base_llm_agent import BaseLLMAgent

from models.character_bible import CharacterBible

from prompts.character.character_bible_prompt import CharacterBiblePrompt

from utils.json_parser import parse_json


class CharacterBibleAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Character Bible Agent")

    def generate_character_bible(self, character):

        return self.run(character)

    def run(self, character):

        self.start()

        print(f"Generating Character Bible: {character.name}")

        prompt = CharacterBiblePrompt.generate(character)

        response = self.think(prompt)

        data = parse_json(response)

        return CharacterBible(
            character_id=data.get("character_id", ""),
            name=data.get("name", ""),
            species=data.get("species", ""),
            role=data.get("role", ""),
            appearance=data.get("appearance", ""),
            clothing=data.get("clothing", ""),
            accessories=data.get("accessories", ""),
            color_palette=data.get("color_palette", ""),
            personality=data.get("personality", ""),
            strengths=data.get("strengths", ""),
            weaknesses=data.get("weaknesses", ""),
            goals=data.get("goals", ""),
            default_expression=data.get("default_expression", ""),
            default_pose=data.get("default_pose", ""),
            movement_style=data.get("movement_style", ""),
            gestures=data.get("gestures", ""),
            voice_style=data.get("voice_style", ""),
            catch_phrase=data.get("catch_phrase", ""),
            image_prompt=data.get("image_prompt", ""),
            negative_prompt=data.get("negative_prompt", "")
        )

    def generate_character_bibles(self, characters):

        character_bibles = []

        for character in characters:

            bible = self.run(character)

            character_bibles.append(bible)

        return character_bibles