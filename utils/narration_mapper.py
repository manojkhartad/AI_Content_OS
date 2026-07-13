# ==========================================================
# Imports
# ==========================================================

from models.narration import Narration
from models.narration import NarrationList


# ==========================================================
# Narration Mapper
# ==========================================================

class NarrationMapper:

    @staticmethod
    def from_json(data: dict) -> NarrationList:

        narrations = []

        for item in data.get("narrations", []):

            narration = Narration(

                scene_id=item.get("scene_id", ""),

                scene_number=item.get("scene_number", 0),

                title=item.get("title", ""),

                narration=item.get("narration", ""),

                word_count=item.get("word_count", 0),

                estimated_duration=item.get(
                    "estimated_duration",
                    0.0
                ),

                audio_file=item.get("audio_file", ""),

                subtitle_file=item.get("subtitle_file", "")

            )

            narrations.append(narration)

        return NarrationList(

            title=data.get("title", ""),

            total_scenes=data.get(
                "total_scenes",
                len(narrations)
            ),

            narrations=narrations

        )