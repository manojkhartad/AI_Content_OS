# ==========================================================
# Imports
# ==========================================================

from agents.base_agent import BaseAgent
from models.narration import Narration
from models.narration import NarrationList


# ==========================================================
# Narration Agent
# ==========================================================

class NarrationAgent(BaseAgent):

    def __init__(self):

        super().__init__("Narration Agent")

    def generate_narrations(
        self,
        scene_list
    ) -> NarrationList:

        return self.run(scene_list)

    def run(
        self,
        scene_list
    ) -> NarrationList:

        self.start()

        print("Narration Generation Started")

        narrations = []

        for scene in scene_list.scenes:

            word_count = len(scene.narration.split())

            estimated_duration = round(
                word_count / 2.5,
                2
            )

            narration = Narration(

                scene_id=scene.scene_id,

                scene_number=scene.scene_number,

                title=scene.title,

                narration=scene.narration,

                word_count=word_count,

                estimated_duration=estimated_duration,

                audio_file="",

                subtitle_file=""

            )

            narrations.append(narration)

            print(
                f"Scene {scene.scene_number} ✓ "
                f"{word_count} words | "
                f"{estimated_duration} sec"
            )

        print()

        return NarrationList(

            title=scene_list.title,

            total_scenes=scene_list.total_scenes,

            narrations=narrations

        )