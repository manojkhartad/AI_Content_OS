# ==========================================================
# Imports
# ==========================================================

import re
from pathlib import Path

from agents.base_agent import BaseAgent
from brain.video_client import VideoClient
from config.paths import VIDEOS_DIR
from config.settings import (
    VIDEO_FPS,
    VIDEO_HEIGHT,
    VIDEO_WIDTH,
)
from exporters.video_exporter import VideoExporter
from models.generated_video import GeneratedVideo


# ==========================================================
# Video Generation Agent
# ==========================================================

class VideoGenerationAgent(BaseAgent):

    def __init__(self):

        super().__init__("Video Generation Agent")

    # ------------------------------------------------------
    # Public API
    # ------------------------------------------------------

    def generate_video(

        self,

        draft,

        generated_images,

        generated_audio

    ):

        return self.run(

            draft,

            generated_images,

            generated_audio

        )

    # ------------------------------------------------------
    # Main
    # ------------------------------------------------------

    def run(

        self,

        draft,

        generated_images,

        generated_audio

    ):

        self.start()

        print("Video Generation Started")

        # --------------------------------------------------
        # Create Scene Maps
        # --------------------------------------------------

        image_map = {

            image.scene_number: image

            for image in generated_images

        }

        audio_map = {

            audio.scene_number: audio

            for audio in generated_audio

        }

        image_scenes = set(image_map.keys())

        audio_scenes = set(audio_map.keys())

        common_scenes = sorted(

            image_scenes & audio_scenes

        )

        missing_images = sorted(

            audio_scenes - image_scenes

        )

        missing_audio = sorted(

            image_scenes - audio_scenes

        )

        if missing_images:

            print("\nMissing Images")

            for scene in missing_images:

                print(f"Scene {scene}")

        if missing_audio:

            print("\nMissing Audio")

            for scene in missing_audio:

                print(f"Scene {scene}")

        if not common_scenes:

            raise RuntimeError(

                "No valid image/audio pairs found."

            )

        # --------------------------------------------------
        # Generate Scene Videos
        # --------------------------------------------------

        scene_videos = []

        completed = []

        failed = []

        skipped = []

        for scene_number in common_scenes:

            image = image_map[scene_number]

            audio = audio_map[scene_number]

            output_path = (

                VIDEOS_DIR /

                f"scene_{scene_number:03d}.mp4"

            )

            # --------------------------------------------------
            # Resume Support
            # --------------------------------------------------

            if output_path.exists():

                print(

                    f"\n✓ Scene {scene_number} Already Exists"

                )

                scene_videos.append(

                    output_path

                )

                completed.append(

                    scene_number

                )

                skipped.append(

                    scene_number

                )

                continue

            print(

                f"\nGenerating Video : Scene {scene_number}"

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

                completed.append(

                    scene_number

                )

                print(

                    f"✓ Scene {scene_number} Video Created"

                )

            except Exception as e:

                print(

                    f"\n❌ Failed : Scene {scene_number}"

                )

                print(e)

                failed.append(

                    scene_number

                )

        # --------------------------------------------------
        # Validation
        # --------------------------------------------------

        if not scene_videos:

            raise RuntimeError(

                "No scene videos were created."

            )

        # --------------------------------------------------
        # Safe File Name
        # --------------------------------------------------

        safe_title = re.sub(

            r"[^A-Za-z0-9_-]+",

            "_",

            draft.title

        ).strip("_")

        final_video = (

            VIDEOS_DIR /

            f"{safe_title}.mp4"

        )

        # --------------------------------------------------
        # Merge Videos
        # --------------------------------------------------

        if final_video.exists():

            print(

                "\n✓ Final Video Already Exists"

            )

        else:

            print(

                "\nCreating Final Video..."

            )

            VideoClient.merge_scene_videos(

                video_paths=scene_videos,

                output_path=final_video

            )

        # --------------------------------------------------
        # Duration
        # --------------------------------------------------

        total_duration = sum(

            audio_map[scene].duration

            for scene in completed

        )

        # --------------------------------------------------
        # Metadata
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

            total_scenes=len(

                completed

            ),

            status="completed"

        )

        VideoExporter.export(

            video

        )

        # --------------------------------------------------
        # Summary
        # --------------------------------------------------

        print("\n===================================")

        print("Video Generation Summary")

        print("===================================")

        print(

            f"Expected Scenes : {len(audio_map)}"

        )

        print(

            f"Completed       : {len(completed)}"

        )

        print(

            f"Skipped         : {len(skipped)}"

        )

        print(

            f"Failed          : {len(failed)}"

        )

        if missing_images:

            print(

                f"Missing Images : {missing_images}"

            )

        if missing_audio:

            print(

                f"Missing Audio  : {missing_audio}"

            )

        if skipped:

            print(

                f"Skipped Scenes : {skipped}"

            )

        if failed:

            print(

                f"Failed Scenes  : {failed}"

            )

        print(

            f"Final Video    : {final_video}"

        )

        print("===================================")

        return video