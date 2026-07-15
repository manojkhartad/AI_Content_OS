# ==========================================================
# Imports
# ==========================================================

from agents.base_agent import BaseAgent
from brain.tts_client import TTSClient
from config.paths import AUDIO_DIR
from exporters.audio_exporter import AudioExporter
from models.generated_audio import GeneratedAudio


# ==========================================================
# TTS Agent
# ==========================================================

class TTSAgent(BaseAgent):

    def __init__(self):
        super().__init__("TTS Agent")

    def generate_audio(self, narration_list):

        return self.run(narration_list)

    def run(self, narration_list):

        self.start()

        print("Audio Generation Started")

        generated_audio = []

        for narration in narration_list.narrations:

            print(
                f"\nGenerating Audio : Scene {narration.scene_number}"
            )

            filename = (
                f"scene_{narration.scene_number:03d}.mp3"
            )

            output_path = AUDIO_DIR / filename

            try:

                # --------------------------------------------------
                # Generate Audio
                # --------------------------------------------------

                TTSClient.generate_audio(
                    text=narration.narration,
                    output_path=output_path
                )

                narration.audio_file = str(output_path)

                # --------------------------------------------------
                # Create GeneratedAudio Model
                # --------------------------------------------------

                audio = GeneratedAudio(

                    scene_id=narration.scene_id,

                    scene_number=narration.scene_number,

                    title=narration.title,

                    narration=narration.narration,

                    audio_path=str(output_path),

                    duration=narration.estimated_duration,

                    voice="en-US-AriaNeural",

                    provider="Microsoft Edge TTS",

                    model="edge-tts",

                    sample_rate=24000,

                    format="mp3"

                )

                # --------------------------------------------------
                # Export Metadata
                # --------------------------------------------------

                AudioExporter.export(audio)

                generated_audio.append(audio)

                print(
                    f"✓ Audio Generated : Scene {narration.scene_number}"
                )

            except Exception as e:

                print(
                    f"\n❌ Failed : Scene {narration.scene_number}"
                )

                print(e)

                continue

        print("\nAudio Generation Completed")

        return generated_audio