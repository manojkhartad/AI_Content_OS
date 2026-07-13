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

IMAGES_DIR = PRODUCTION_DIR / "images"

VIDEOS_DIR = PRODUCTION_DIR / "videos"


# ==========================================================
# Auto Create Required Directories
# ==========================================================

for folder in [
    PRODUCTION_DIR,
    STORIES_DIR,
    CHARACTERS_DIR,
    SCENES_DIR,
    IMAGES_DIR,
    VIDEOS_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)