# ==========================================================
# Imports
# ==========================================================

import re
from pathlib import Path

from agents.base_agent import BaseAgent
from brain.video_client import VideoClient
from config.paths import VIDEOS_DIR
from exporters.video_exporter import VideoExporter
from models.generated_video import GeneratedVideo
from config.settings import (
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
    VIDEO_FPS,
)


# ==========================================================
# Video Generation Agent
# ==========================================================

class VideoGenerationAgent(BaseAgent):

    def __init__(self):

        super().__init__("Video Generation Agent")

    def generate_video(

        self,

        draft,

        generated_images,

        generated_audio

    ):

        print("Video Generation Started")

        scene_videos = []

        # --------------------------------------------------
        # Create Scene Videos
        # --------------------------------------------------

        for image, audio in zip(
            generated_images,
            generated_audio
        ):

            print(
                f"\nGenerating Video : Scene {image.scene_number}"
            )

            output_path = (
                VIDEOS_DIR /
                f"scene_{image.scene_number:03d}.mp4"
            )

            try:

                VideoClient.create_scene_video(

                    image_path=Path(
                        image.image_path
                    ),

                    audio_path=Path(
                        audio.audio_path
                    ),

                    output_path=output_path

                )

                scene_videos.append(
                    output_path
                )

                print(
                    f"✓ Scene {image.scene_number} Video Created"
                )

            except Exception as e:

                print(
                    f"\n❌ Failed : Scene {image.scene_number}"
                )

                print(e)

                continue

        # --------------------------------------------------
        # Stop if no videos were created
        # --------------------------------------------------

        if not scene_videos:

            raise RuntimeError(
                "No scene videos were created."
            )

        # --------------------------------------------------
        # Create Safe File Name
        # --------------------------------------------------

        safe_title = re.sub(
            r"[^A-Za-z0-9_-]+",
            "_",
            draft.title
        ).strip("_")

        # --------------------------------------------------
        # Merge Videos
        # --------------------------------------------------

        print("\nCreating Final Video...")

        final_video = (
            VIDEOS_DIR /
            f"{safe_title}.mp4"
        )

        VideoClient.merge_scene_videos(

            video_paths=scene_videos,

            output_path=final_video

        )

        # --------------------------------------------------
        # Calculate Total Duration
        # --------------------------------------------------

        total_duration = sum(
            audio.duration
            for audio in generated_audio
        )

        # --------------------------------------------------
        # Video Metadata
        # --------------------------------------------------

        video = GeneratedVideo(

            title=draft.title,

            video_path=str(
                final_video
            ),

            width=VIDEO_WIDTH,

            height=VIDEO_HEIGHT,

            fps=VIDEO_FPS,

            duration=round(
                total_duration,
                2
            ),

            codec="H.264",

            format="MP4",

            provider="FFmpeg",

            total_scenes=len(scene_videos),

            status="completed"

        )

        VideoExporter.export(
            video
        )

        print("\n===================================")
        print("Video Generation Completed")
        print(f"Saved : {final_video}")
        print("===================================")

        return video