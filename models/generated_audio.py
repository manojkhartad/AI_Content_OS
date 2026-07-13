# ==========================================================
# Imports
# ==========================================================

from dataclasses import dataclass


# ==========================================================
# Generated Audio
# ==========================================================

@dataclass
class GeneratedAudio:

    # Scene Information

    scene_id: str

    scene_number: int

    title: str

    # Narration

    narration: str

    # Audio

    audio_path: str

    duration: float

    voice: str

    provider: str

    model: str

    sample_rate: int

    format: str