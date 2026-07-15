# ==========================================================
# Imports
# ==========================================================

from google import genai

from brain.exceptions import LLMGenerationError
from brain.fallback_manager import FallbackManager
from brain.model_registry import ModelRegistry
from brain.prompt_cache import prompt_cache
from brain.response_parser import ResponseParser
from brain.retry_manager import RetryManager
from brain.usage_tracker import UsageTracker

from config.settings import GEMINI_API_KEY

from utils.logger import logger


# ==========================================================
# LLM Client
# ==========================================================

class LLMClient:

    def __init__(self):

        self.client = genai.Client(

            api_key=GEMINI_API_KEY

        )

        self.models = ModelRegistry.get_models()

        self.usage_tracker = UsageTracker()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    def generate(

        self,

        prompt: str,

    ):

        # --------------------------------------------------
        # Prompt Cache
        # --------------------------------------------------

        cached_response = prompt_cache.get(

            prompt

        )

        if cached_response is not None:

            print(

                "\n✓ Prompt Cache Hit"

            )

            logger.info(

                "Prompt served from cache."

            )

            return cached_response

        print(

            "\nPrompt Cache Miss"

        )

        logger.info(

            "Prompt cache miss."

        )

        # --------------------------------------------------
        # Model Fallback
        # --------------------------------------------------

        models = FallbackManager.get_models(

            self.models

        )

        last_error = None

        # --------------------------------------------------
        # Try Models
        # --------------------------------------------------

        for attempt, model in enumerate(

            models

        ):

            start_time = self.usage_tracker.start_request(

                model

            )

            try:

                print(

                    f"\nTrying Model : {model}"

                )

                logger.info(

                    f"Trying model : {model}"

                )

                response = self.client.models.generate_content(

                    model=model,

                    contents=prompt,

                )

                parsed_response = ResponseParser.parse(

                    response

                )

                prompt_cache.set(

                    prompt,

                    parsed_response,

                )

                self.usage_tracker.end_request(

                    start_time,

                    success=True,

                )

                print(

                    f"✓ Success : {model}"

                )

                logger.info(

                    f"Model succeeded : {model}"

                )

                return parsed_response

            except Exception as error:

                self.usage_tracker.end_request(

                    start_time,

                    success=False,

                )

                logger.exception(

                    str(error)

                )

                last_error = error

                if RetryManager.should_retry(

                    error

                ):

                    print(

                        f"\nRetryable Error : {model}"

                    )

                    print(

                        error

                    )

                    RetryManager.wait(

                        attempt

                    )

                    continue

                print(

                    f"\nNon-Retryable Error : {model}"

                )

                raise

        # --------------------------------------------------
        # Failed
        # --------------------------------------------------

        logger.error(

            "All LLM models failed."

        )

        raise LLMGenerationError(

            "All configured LLM models failed.\n"

            f"Last Error : {last_error}"

        )