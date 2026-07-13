# ==========================================================
# Imports
# ==========================================================

import json
from dataclasses import asdict

from config.paths import SCENES_DIR


# ==========================================================
# Scene Exporter
# ==========================================================

class SceneExporter:

    @staticmethod
    def export(scene_list):

        filename = (
            scene_list.title
            .replace(" ", "_")
            .replace("/", "_")
        )

        filepath = SCENES_DIR / f"{filename}_scenes.json"

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                asdict(scene_list),
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\nScenes exported successfully.")
        print(filepath)