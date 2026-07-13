# ==========================================================
# Imports
# ==========================================================

import asyncio
from pathlib import Path

import edge_tts

from config.settings import TTS_PROVIDER


# ==========================================================
# TTS Client
# ==========================================================

class TTSClient:

    DEFAULT_VOICE = "en-US-AvaNeural"

    @staticmethod
    async def _generate(
        text: str,
        output_path: Path,
        voice: str
    ):

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice
        )

        await communicate.save(
            str(output_path)
        )

    @staticmethod
    def generate_audio(
        text: str,
        output_path: Path,
        voice: str = None
    ):

        if TTS_PROVIDER != "edge":
            raise ValueError(
                f"Unsupported TTS Provider : {TTS_PROVIDER}"
            )

        if voice is None:
            voice = TTSClient.DEFAULT_VOICE

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        print("\nGenerating Audio...")

        asyncio.run(
            TTSClient._generate(
                text=text,
                output_path=output_path,
                voice=voice
            )
        )

        print(f"Audio Saved : {output_path}")

        return output_path