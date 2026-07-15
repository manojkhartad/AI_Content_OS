# ==========================================================
# Imports
# ==========================================================

from utils.logger import Logger


# ==========================================================
# Model Registry
# ==========================================================

class ModelRegistry:

    logger = Logger.get_logger()

    # ------------------------------------------------------
    # Registry
    # ------------------------------------------------------

    _MODELS = {

        "gemini": [

            "models/gemma-4-31b-it",

            "models/gemini-3.5-flash",

            "models/gemini-3.1-flash-lite",

        ],

        "openai": [

            "gpt-5.5",

            "gpt-5.5-mini",

        ],

        "claude": [

            "claude-sonnet-4",

        ],

    }

    # ------------------------------------------------------
    # Enabled Providers
    # ------------------------------------------------------

    _ENABLED = {

        "gemini": True,

        "openai": False,

        "claude": False,

    }

    # ------------------------------------------------------
    # Get Active Models
    # ------------------------------------------------------

    @classmethod
    def get_models(cls):

        models = []

        for provider, enabled in cls._ENABLED.items():

            if not enabled:

                continue

            models.extend(cls._MODELS.get(provider, []))

        # Remove duplicates while preserving order
        models = list(dict.fromkeys(models))

        cls.logger.info(
            f"Loaded {len(models)} models."
        )

        return models

    # ------------------------------------------------------
    # Get Provider Models
    # ------------------------------------------------------

    @classmethod
    def get_provider_models(

        cls,

        provider: str,

    ):

        return list(

            cls._MODELS.get(provider, [])

        )

    # ------------------------------------------------------
    # Enable Provider
    # ------------------------------------------------------

    @classmethod
    def enable_provider(

        cls,

        provider: str,

    ):

        if provider in cls._ENABLED:

            cls._ENABLED[provider] = True

            cls.logger.info(

                f"Enabled provider : {provider}"

            )

    # ------------------------------------------------------
    # Disable Provider
    # ------------------------------------------------------

    @classmethod
    def disable_provider(

        cls,

        provider: str,

    ):

        if provider in cls._ENABLED:

            cls._ENABLED[provider] = False

            cls.logger.info(

                f"Disabled provider : {provider}"

            )

    # ------------------------------------------------------
    # Add Model
    # ------------------------------------------------------

    @classmethod
    def add_model(

        cls,

        provider: str,

        model: str,

    ):

        if provider not in cls._MODELS:

            cls._MODELS[provider] = []

            cls._ENABLED[provider] = True

        if model not in cls._MODELS[provider]:

            cls._MODELS[provider].append(model)

            cls.logger.info(

                f"Added model : {model}"

            )

    # ------------------------------------------------------
    # Remove Model
    # ------------------------------------------------------

    @classmethod
    def remove_model(

        cls,

        provider: str,

        model: str,

    ):

        if (

            provider in cls._MODELS

            and model in cls._MODELS[provider]

        ):

            cls._MODELS[provider].remove(model)

            cls.logger.info(

                f"Removed model : {model}"

            )

    # ------------------------------------------------------
    # Get Registry
    # ------------------------------------------------------

    @classmethod
    def registry(cls):

        return {

            provider: list(models)

            for provider, models

            in cls._MODELS.items()

        }

    # ------------------------------------------------------
    # Reset
    # ------------------------------------------------------

    @classmethod
    def reset(cls):

        cls._ENABLED = {

            "gemini": True,

            "openai": False,

            "claude": False,

        }

        cls.logger.info(

            "Model registry reset."

        )