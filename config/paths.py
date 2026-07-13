from pathlib import Path


# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ==========================================================
# Production Root
# ==========================================================

PRODUCTION_DIR = PROJECT_ROOT / "production"


# ==========================================================
# Production Output Folders
# ==========================================================

STORIES_DIR = PRODUCTION_DIR / "stories"

CHARACTERS_DIR = PRODUCTION_DIR / "characters"

SCENES_DIR = PRODUCTION_DIR / "scenes"

NARRATIONS_DIR = PRODUCTION_DIR / "narrations"

IMAGE_PROMPTS_DIR = PRODUCTION_DIR / "image_prompts"

IMAGES_DIR = PRODUCTION_DIR / "images"

AUDIO_DIR = PRODUCTION_DIR / "audio"

SUBTITLES_DIR = PRODUCTION_DIR / "subtitles"

VIDEOS_DIR = PRODUCTION_DIR / "videos"


# ==========================================================
# Auto Create Required Directories
# ==========================================================

for folder in [
    PRODUCTION_DIR,
    STORIES_DIR,
    CHARACTERS_DIR,
    SCENES_DIR,
    NARRATIONS_DIR,
    IMAGE_PROMPTS_DIR,
    IMAGES_DIR,
    AUDIO_DIR,
    SUBTITLES_DIR,
    VIDEOS_DIR,
]:
    folder.mkdir(
        parents=True,
        exist_ok=True
    )