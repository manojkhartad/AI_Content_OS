# ==========================================================
# Imports
# ==========================================================

import subprocess
from pathlib import Path

from config.settings import (
    CAMERA_FRAME_COUNT,
    CAMERA_MAX_ZOOM,
    CAMERA_ZOOM_SPEED,
    FFMPEG_PATH,
    VIDEO_FPS,
    VIDEO_HEIGHT,
    VIDEO_WIDTH,
)


# ==========================================================
# Video Client (FFmpeg)
# ==========================================================

class VideoClient:

    # ------------------------------------------------------
    # Validate File
    # ------------------------------------------------------

    @staticmethod
    def _validate_file(path: Path, name: str):

        if not path.exists():

            raise FileNotFoundError(
                f"{name} not found : {path}"
            )

    # ------------------------------------------------------
    # Execute FFmpeg
    # ------------------------------------------------------

    @staticmethod
    def _run_ffmpeg(command):

        try:

            subprocess.run(

                command,

                check=True,

                capture_output=True,

                text=True

            )

        except subprocess.CalledProcessError as e:

            print("\nFFmpeg Error\n")

            if e.stderr:

                print(e.stderr)

            raise RuntimeError(
                "FFmpeg execution failed."
            ) from e

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

        VideoClient._validate_file(
            image_path,
            "Image"
        )

        VideoClient._validate_file(
            audio_path,
            "Audio"
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

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
                f"z='min(zoom+{CAMERA_ZOOM_SPEED},{CAMERA_MAX_ZOOM})':"
                f"d={CAMERA_FRAME_COUNT}:"
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

        VideoClient._run_ffmpeg(command)

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

        if not video_paths:

            raise ValueError(
                "No scene videos available."
            )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        list_file = (
            output_path.parent / "videos.txt"
        )

        try:

            with open(

                list_file,

                "w",

                encoding="utf-8"

            ) as file:

                for video in video_paths:

                    VideoClient._validate_file(
                        video,
                        "Scene Video"
                    )

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

            VideoClient._run_ffmpeg(command)

        finally:

            if list_file.exists():

                list_file.unlink()

        print(
            f"Final Video Saved : {output_path}"
        )