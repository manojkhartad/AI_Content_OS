# ==========================================================
# Imports
# ==========================================================

from dataclasses import dataclass, field


# ==========================================================
# Narration
# ==========================================================

@dataclass
class Narration:

    scene_id: str
    scene_number: int
    title: str

    narration: str

    word_count: int = 0

    estimated_duration: float = 0.0

    audio_file: str = ""

    subtitle_file: str = ""


# ==========================================================
# Narration List
# ==========================================================

@dataclass
class NarrationList:

    title: str

    total_scenes: int

    narrations: list[Narration] = field(default_factory=list)