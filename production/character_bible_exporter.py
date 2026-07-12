import json
from pathlib import Path
from dataclasses import asdict


class CharacterBibleExporter:

    @staticmethod
    def export(character_bibles):

        production_folder = Path("production")
        characters_folder = production_folder / "characters"

        characters_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        for character in character_bibles:

            filename = (
                character.name
                .replace(" ", "_")
                .replace("/", "_")
            )

            filepath = characters_folder / f"{filename}.json"

            with open(
                filepath,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    asdict(character),
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        print("\nCharacter Bibles exported successfully.")
        print(characters_folder)