# ==========================================================
# Imports
# ==========================================================

import json
from dataclasses import asdict

from config.paths import CHARACTERS_DIR


# ==========================================================
# Character Bible Exporter
# ==========================================================

class CharacterBibleExporter:

    @staticmethod
    def export(character_bibles):

        for character in character_bibles:

            filename = (
                character.name
                .replace(" ", "_")
                .replace("/", "_")
            )

            filepath = CHARACTERS_DIR / f"{filename}.json"

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
        print(CHARACTERS_DIR)