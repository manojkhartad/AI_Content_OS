# ==========================================================
# Imports
# ==========================================================

import random
import time

from google.genai.errors import (
    ClientError,
    ServerError,
)


# ==========================================================
# Retry Manager
# ==========================================================

class RetryManager:

    MAX_RETRIES = 5

    BASE_DELAY = 2

    MAX_DELAY = 30

    # ------------------------------------------------------
    # Should Retry
    # ------------------------------------------------------

    @staticmethod
    def should_retry(error) -> bool:

        if isinstance(error, ServerError):

            return True

        if isinstance(error, ClientError):

            status = getattr(

                error,

                "status_code",

                None

            )

            if status in (

                408,

                409,

                425,

                429,

                500,

                502,

                503,

                504,

            ):

                return True

        return False

    # ------------------------------------------------------
    # Retry Delay
    # ------------------------------------------------------

    @classmethod
    def wait(cls, attempt: int):

        delay = min(

            cls.BASE_DELAY * (2 ** attempt),

            cls.MAX_DELAY

        )

        jitter = random.uniform(

            0,

            1

        )

        total_delay = delay + jitter

        print(

            f"\nRetrying in {total_delay:.2f} seconds..."

        )

        time.sleep(total_delay)