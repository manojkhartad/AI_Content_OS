# ==========================================================
# Imports
# ==========================================================

import random

from models.camera_effect import CameraEffect
from config.settings import (
    VIDEO_FPS,
    CAMERA_ZOOM_SPEED,
    CAMERA_MAX_ZOOM,
)


# ==========================================================
# Camera Effects
# ==========================================================

class CameraEffects:

    @staticmethod
    def zoom_in():

        return CameraEffect(

            name="zoom_in",

            filter=(

                f"scale=1920:1080,"
                f"zoompan="
                f"z='min(zoom+{CAMERA_ZOOM_SPEED},{CAMERA_MAX_ZOOM})':"
                f"d=10000:"
                f"x='iw/2-(iw/zoom/2)':"
                f"y='ih/2-(ih/zoom/2)',"
                f"fps={VIDEO_FPS}"

            )

        )

    @staticmethod
    def static():

        return CameraEffect(

            name="static",

            filter=(

                f"scale=1920:1080,"
                f"fps={VIDEO_FPS}"

            )

        )

    @staticmethod
    def random():

        return random.choice(

            [

                CameraEffects.zoom_in(),
                CameraEffects.static(),

            ]

        )