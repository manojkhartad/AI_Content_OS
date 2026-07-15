# ==========================================================
# Imports
# ==========================================================

import time

from brain.llm_client import LLMClient
from config.settings import LLM_PROVIDER
from utils.logger import Logger


# ==========================================================
# LLM Router
# ==========================================================

class LLMRouter:

    def __init__(self):

        self.provider = LLM_PROVIDER

        self.client = LLMClient()

        self.logger = Logger.get_logger()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    def generate(
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

        print("\n===================================")
        print("LLM Router")
        print("===================================")
        print(
            f"Provider : {self.provider}"
        )

        self.logger.info(
            f"Provider : {self.provider}"
        )

        start_time = time.perf_counter()

        try:

            response = self.client.generate(
                prompt
            )

            elapsed = round(
                time.perf_counter() - start_time,
                2,
            )

            print(
                f"✓ Completed ({elapsed} sec)"
            )

            self.logger.info(
                f"Completed in {elapsed} sec"
            )

            return response

        except Exception as error:

            elapsed = round(
                time.perf_counter() - start_time,
                2,
            )

            print(
                f"❌ Failed ({elapsed} sec)"
            )

            print(error)

            self.logger.error(
                f"Failed in {elapsed} sec"
            )

            self.logger.error(
                str(error)
            )

            raise RuntimeError(

                f"LLM Router Error : {error}"

            ) from error

    # ------------------------------------------------------
    # Provider
    # ------------------------------------------------------

    def get_provider(self):

        return self.provider

    # ------------------------------------------------------
    # Change Provider
    # ------------------------------------------------------

    def set_provider(
        self,
        provider: str,
    ):

        self.provider = provider

        self.logger.info(
            f"Provider changed to {provider}"
        )

    # ------------------------------------------------------
    # Reset
    # ------------------------------------------------------

    def reset(self):

        self.provider = LLM_PROVIDER

        self.client = LLMClient()

        self.logger.info(
            "LLM Router reset."
        )