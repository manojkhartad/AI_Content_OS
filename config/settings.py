# ==========================================================
# Imports
# ==========================================================

import os

from dotenv import load_dotenv


# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()


# ==========================================================
# API Keys
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

FAL_API_KEY = os.getenv("FAL_API_KEY", "")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")


# ==========================================================
# Providers
# ==========================================================

LLM_PROVIDER = "gemini"

IMAGE_PROVIDER = "pollinations"
# IMAGE_PROVIDER = "fal"

TTS_PROVIDER = "edge"
# TTS_PROVIDER = "elevenlabs"

VIDEO_PROVIDER = "ffmpeg"


# ==========================================================
# Default Models
# ==========================================================

LLM_MODEL = "models/gemma-4-31b-it"

IMAGE_MODEL = "flux"

TTS_MODEL = "en-US-AriaNeural"

VIDEO_ENGINE = "ffmpeg"


# ==========================================================
# Batch Settings
# ==========================================================

IMAGE_PROMPT_BATCH_SIZE = 5

CHARACTER_BIBLE_BATCH_SIZE = 5


# ==========================================================
# Image Generation Workers
# ==========================================================

# Pollinations free API gets rate-limited easily.
# Keep this low for maximum reliability.

if IMAGE_PROVIDER == "pollinations":

    IMAGE_GENERATION_WORKERS = 1

else:

    IMAGE_GENERATION_WORKERS = 4


# ==========================================================
# Image Generation Settings
# ==========================================================

IMAGE_WIDTH = 1024

IMAGE_HEIGHT = 576

IMAGE_TIMEOUT = 180

IMAGE_MAX_RETRIES = 5

IMAGE_RETRY_DELAYS = [
    2,
    5,
    10,
    20,
    30,
]


# ==========================================================
# FFmpeg
# ==========================================================

FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"


# ==========================================================
# Video Settings
# ==========================================================

VIDEO_WIDTH = 1024

VIDEO_HEIGHT = 576

VIDEO_FPS = 30


# ==========================================================
# Camera Settings
# ==========================================================

CAMERA_DEFAULT_EFFECT = "random"

CAMERA_ZOOM_SPEED = 0.0008

CAMERA_MAX_ZOOM = 1.15

CAMERA_FRAME_COUNT = 10000


# ==========================================================
# Validation
# ==========================================================

if LLM_PROVIDER == "gemini" and not GEMINI_API_KEY:

    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )


if IMAGE_PROVIDER == "fal" and not FAL_API_KEY:

    raise ValueError(
        "FAL_API_KEY not found in .env file"
    )


if TTS_PROVIDER == "elevenlabs" and not ELEVENLABS_API_KEY:

    raise ValueError(
        "ELEVENLABS_API_KEY not found in .env file"
    )


if VIDEO_PROVIDER == "ffmpeg":

    if not os.path.exists(FFMPEG_PATH):

        raise ValueError(
            f"FFmpeg not found : {FFMPEG_PATH}"
        )