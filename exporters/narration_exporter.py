# ==========================================================
# Imports
# ==========================================================

import json

from config.paths import NARRATIONS_DIR


# ==========================================================
# Narration Exporter
# ==========================================================

class NarrationExporter:

    @staticmethod
    def export(narration_list):

        output_file = (
            NARRATIONS_DIR /
            f"{narration_list.title.replace(' ', '_')}_narrations.json"
        )

        data = {
            "title": narration_list.title,
            "total_scenes": narration_list.total_scenes,
            "narrations": []
        }

        for narration in narration_list.narrations:

            data["narrations"].append({

                "scene_id": narration.scene_id,

                "scene_number": narration.scene_number,

                "title": narration.title,

                "narration": narration.narration,

                "word_count": narration.word_count,

                "estimated_duration": narration.estimated_duration,

                "audio_file": narration.audio_file,

                "subtitle_file": narration.subtitle_file

            })

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\nNarrations exported successfully.")
        print(output_file)

        return output_file