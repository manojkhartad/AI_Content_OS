# ==========================================================
# Imports
# ==========================================================

import json

from config.paths import AUDIO_DIR
from models.generated_audio import GeneratedAudio


# ==========================================================
# Audio Exporter
# ==========================================================

class AudioExporter:

    @staticmethod
    def export(audio: GeneratedAudio):

        output_file = (
            AUDIO_DIR /
            f"scene_{audio.scene_number:03d}.json"
        )

        data = {

            "scene_id": audio.scene_id,

            "scene_number": audio.scene_number,

            "title": audio.title,

            "narration": audio.narration,

            "audio_path": audio.audio_path,

            "duration": audio.duration,

            "voice": audio.voice,

            "provider": audio.provider,

            "model": audio.model,

            "sample_rate": audio.sample_rate,

            "format": audio.format

        }

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print("\nAudio Exported Successfully")

        print(f"Scene : {audio.scene_number}")

        print(f"Saved : {output_file}")