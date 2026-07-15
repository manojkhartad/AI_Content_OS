# ==========================================================
# Imports
# ==========================================================

import threading
import time

from utils.logger import Logger


# ==========================================================
# Fallback Manager
# ==========================================================

class FallbackManager:

    """
    Handles temporary blacklisting of failed LLM models.

    If a model repeatedly fails, it is skipped for a cooldown
    period before becoming available again.
    """

    # ------------------------------------------------------
    # Configuration
    # ------------------------------------------------------

    COOLDOWN = 300  # seconds

    # ------------------------------------------------------
    # Internal State
    # ------------------------------------------------------

    _failed_models = {}

    _lock = threading.Lock()

    _logger = Logger.get_logger()

    # ------------------------------------------------------
    # Get Available Models
    # ------------------------------------------------------

    @classmethod
    def get_models(cls, models: list[str]) -> list[str]:

        with cls._lock:

            cls._cleanup()

            available = []

            seen = set()

            for model in models:

                if model in seen:
                    continue

                seen.add(model)

                if model not in cls._failed_models:

                    available.append(model)

            # If every model is cooling down,
            # allow all models again.
            if not available:

                cls._logger.warning(
                    "All models are currently in cooldown. "
                    "Using original model list."
                )

                return list(dict.fromkeys(models))

            return available

    # ------------------------------------------------------
    # Mark Failed
    # ------------------------------------------------------

    @classmethod
    def mark_failed(
        cls,
        model: str,
    ):

        with cls._lock:

            cls._failed_models[model] = time.time()

            cls._logger.warning(
                f"Model marked as failed : {model}"
            )

    # ------------------------------------------------------
    # Mark Success
    # ------------------------------------------------------

    @classmethod
    def mark_success(
        cls,
        model: str,
    ):

        with cls._lock:

            if model in cls._failed_models:

                del cls._failed_models[model]

                cls._logger.info(
                    f"Model recovered : {model}"
                )

    # ------------------------------------------------------
    # Cleanup Expired Models
    # ------------------------------------------------------

    @classmethod
    def _cleanup(cls):

        now = time.time()

        expired = []

        for model, failed_at in cls._failed_models.items():

            if now - failed_at >= cls.COOLDOWN:

                expired.append(model)

        for model in expired:

            del cls._failed_models[model]

            cls._logger.info(
                f"Cooldown expired : {model}"
            )

    # ------------------------------------------------------
    # Status
    # ------------------------------------------------------

    @classmethod
    def status(cls) -> dict:

        with cls._lock:

            cls._cleanup()

            return dict(cls._failed_models)

    # ------------------------------------------------------
    # Is Failed
    # ------------------------------------------------------

    @classmethod
    def is_failed(
        cls,
        model: str,
    ) -> bool:

        with cls._lock:

            cls._cleanup()

            return model in cls._failed_models

    # ------------------------------------------------------
    # Reset
    # ------------------------------------------------------

    @classmethod
    def reset(cls):

        with cls._lock:

            cls._failed_models.clear()

            cls._logger.info(
                "Fallback manager reset."
            )