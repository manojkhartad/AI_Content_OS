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

TTS_PROVIDER = "edge"

VIDEO_PROVIDER = "ffmpeg"


# ==========================================================
# Default Models
# ==========================================================

LLM_MODEL = "models/gemma-4-31b-it"

IMAGE_MODEL = "flux"

TTS_MODEL = "en-US-AriaNeural"

VIDEO_ENGINE = "ffmpeg"


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
# Validation
# ==========================================================

if LLM_PROVIDER == "gemini" and not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")


if VIDEO_PROVIDER == "ffmpeg":
    if not os.path.exists(FFMPEG_PATH):
        raise ValueError(
            f"FFmpeg not found : {FFMPEG_PATH}"
        )