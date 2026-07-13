# ==========================================================
# Imports
# ==========================================================

import subprocess
from pathlib import Path

from config.settings import (
    FFMPEG_PATH,
    VIDEO_FPS,
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
)


# ==========================================================
# Video Client (FFmpeg)
# ==========================================================

class VideoClient:

    # ------------------------------------------------------
    # Image + Audio -> Scene Video
    # ------------------------------------------------------

    @staticmethod
    def create_scene_video(

        image_path: Path,
        audio_path: Path,
        output_path: Path

    ):

        print("\nGenerating Scene Video...")

        command = [

            FFMPEG_PATH,

            "-y",

            "-loop", "1",

            "-i", str(image_path),

            "-i", str(audio_path),

            "-vf",

            (
                f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT},"
                f"zoompan="
                f"z='min(zoom+0.0008,1.15)':"
                f"d=10000:"
                f"x='iw/2-(iw/zoom/2)':"
                f"y='ih/2-(ih/zoom/2)',"
                f"fps={VIDEO_FPS}"
            ),

            "-c:v", "libx264",

            "-preset", "medium",

            "-tune", "stillimage",

            "-pix_fmt", "yuv420p",

            "-c:a", "aac",

            "-b:a", "192k",

            "-shortest",

            "-movflags", "+faststart",

            str(output_path)

        ]

        subprocess.run(
            command,
            check=True
        )

        print(
            f"Scene Video Saved : {output_path}"
        )

    # ------------------------------------------------------
    # Merge Scene Videos
    # ------------------------------------------------------

    @staticmethod
    def merge_scene_videos(

        video_paths: list[Path],

        output_path: Path

    ):

        print("\nMerging Scene Videos...")

        list_file = output_path.parent / "videos.txt"

        with open(

            list_file,

            "w",

            encoding="utf-8"

        ) as file:

            for video in video_paths:

                file.write(
                    f"file '{video.resolve()}'\n"
                )

        command = [

            FFMPEG_PATH,

            "-y",

            "-f", "concat",

            "-safe", "0",

            "-i", str(list_file),

            "-c", "copy",

            "-movflags", "+faststart",

            str(output_path)

        ]

        subprocess.run(

            command,

            check=True

        )

        if list_file.exists():

            list_file.unlink()

        print(
            f"Final Video Saved : {output_path}"
        )