# ==========================================================
# Imports
# ==========================================================

from models.scene import Scene, SceneList


# ==========================================================
# Scene Mapper
# ==========================================================

class SceneMapper:

    @staticmethod
    def from_json(data: dict) -> SceneList:

        scenes = []

        for item in data.get("scenes", []):

            scene = Scene(
                scene_id=item.get("scene_id", ""),
                scene_number=item.get("scene_number", 0),
                title=item.get("title", ""),
                summary=item.get("summary", ""),
                purpose=item.get("purpose", ""),
                location=item.get("location", ""),
                time_of_day=item.get("time_of_day", ""),
                characters=item.get("characters", []),
                narration=item.get("narration", ""),
                dialogue=item.get("dialogue", ""),
                emotion=item.get("emotion", ""),
                visual_notes=item.get("visual_notes", ""),
                continuity_notes=item.get("continuity_notes", "")
            )

            scenes.append(scene)

        return SceneList(
            title=data.get("title", ""),
            total_scenes=data.get("total_scenes", len(scenes)),
            scenes=scenes
        )