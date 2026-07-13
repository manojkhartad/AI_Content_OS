# ==========================================================
# Imports
# ==========================================================

from dataclasses import dataclass, field


# ==========================================================
# Scene Model
# ==========================================================

@dataclass
class Scene:

    # Basic Information
    scene_id: str
    scene_number: int
    title: str

    # Story Information
    summary: str
    purpose: str

    # Environment
    location: str
    time_of_day: str

    # Characters
    characters: list[str] = field(default_factory=list)

    # Story Content
    narration: str = ""
    dialogue: str = ""

    # Emotion
    emotion: str = ""

    # Visual Direction
    visual_notes: str = ""

    # Continuity
    continuity_notes: str = ""


# ==========================================================
# Scene Collection
# ==========================================================

@dataclass
class SceneList:

    title: str
    total_scenes: int
    scenes: list[Scene] = field(default_factory=list)