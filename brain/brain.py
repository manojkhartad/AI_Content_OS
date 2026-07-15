# ==========================================================
# Imports
# ==========================================================

import time

from brain.llm_router import LLMRouter
from utils.logger import Logger


# ==========================================================
# Brain
# ==========================================================

class Brain:

    def __init__(self):

        self.router = LLMRouter()

        self.logger = Logger.get_logger()

        self.total_requests = 0

        self.successful_requests = 0

        self.failed_requests = 0

    # ------------------------------------------------------
    # Think
    # ------------------------------------------------------

    def think(
        self,
        prompt: str,
    ):

        if not isinstance(prompt, str):

            raise TypeError(
                "Prompt must be a string."
            )

        prompt = prompt.strip()

        if not prompt:

            raise ValueError(
                "Prompt cannot be empty."
            )

        self.total_requests += 1

        print("\n===================================")
        print("Brain")
        print("===================================")
        print("Thinking...")

        self.logger.info(
            "Brain request started."
        )

        start_time = time.perf_counter()

        try:

            response = self.router.generate(
                prompt
            )

            elapsed = round(

                time.perf_counter()
                - start_time,

                2,

            )

            self.successful_requests += 1

            print(
                f"✓ Brain Finished ({elapsed} sec)"
            )

            self.logger.info(
                f"Completed in {elapsed} sec"
            )

            return response

        except Exception as error:

            elapsed = round(

                time.perf_counter()
                - start_time,

                2,

            )

            self.failed_requests += 1

            print(
                f"❌ Brain Failed ({elapsed} sec)"
            )

            print(error)

            self.logger.error(
                str(error)
            )

            raise RuntimeError(

                f"Brain Error : {error}"

            ) from error

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    def stats(self):

        return {

            "total_requests": self.total_requests,

            "successful_requests": self.successful_requests,

            "failed_requests": self.failed_requests,

            "provider": self.router.get_provider(),

        }

    # ------------------------------------------------------
    # Health
    # ------------------------------------------------------

    def health(self):

        return {

            "status": "healthy",

            "provider": self.router.get_provider(),

            "requests": self.total_requests,

        }

    # ------------------------------------------------------
    # Reset
    # ------------------------------------------------------

    def reset(self):

        self.router.reset()

        self.total_requests = 0

        self.successful_requests = 0

        self.failed_requests = 0

        self.logger.info(
            "Brain reset."
        )