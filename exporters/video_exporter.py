# ==========================================================
# Imports
# ==========================================================

import json
from dataclasses import asdict

from config.paths import VIDEOS_DIR


# ==========================================================
# Video Exporter
# ==========================================================

class VideoExporter:

    @staticmethod
    def export(video):

        output_file = (
            VIDEOS_DIR /
            f"{video.title.replace(' ', '_')}.json"
        )

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                asdict(video),

                file,

                indent=4,

                ensure_ascii=False

            )

        print("\nVideo Exported Successfully")

        print(
            f"Saved : {output_file}"
        )