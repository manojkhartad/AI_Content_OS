# ==========================================================
# Imports
# ==========================================================

import json
import re

from utils.logger import Logger


# ==========================================================
# Response Parser
# ==========================================================

class ResponseParser:

    logger = Logger.get_logger()

    # ------------------------------------------------------
    # Parse
    # ------------------------------------------------------

    @classmethod
    def parse(
        cls,
        response,
    ):

        if response is None:

            cls.logger.error(
                "Received empty response."
            )

            return ""

        # ----------------------------------------------
        # Gemini Response
        # ----------------------------------------------

        if hasattr(response, "text"):

            text = response.text

        else:

            text = str(response)

        if text is None:

            return ""

        text = text.strip()

        if not text:

            cls.logger.error(
                "Response text is empty."
            )

            return ""

        # ----------------------------------------------
        # Remove Markdown Code Blocks
        # ----------------------------------------------

        text = cls._remove_markdown(text)

        # ----------------------------------------------
        # Try JSON
        # ----------------------------------------------

        parsed = cls._try_json(text)

        if parsed is not None:

            return parsed

        # ----------------------------------------------
        # Return Plain Text
        # ----------------------------------------------

        return text

    # ------------------------------------------------------
    # Remove Markdown
    # ------------------------------------------------------

    @staticmethod
    def _remove_markdown(
        text: str,
    ):

        pattern = r"```(?:json)?\s*(.*?)```"

        match = re.search(

            pattern,

            text,

            re.DOTALL | re.IGNORECASE,

        )

        if match:

            return match.group(1).strip()

        return text

    # ------------------------------------------------------
    # Try JSON
    # ------------------------------------------------------

    @classmethod
    def _try_json(
        cls,
        text: str,
    ):

        try:

            return json.loads(text)

        except Exception:

            pass

        # ----------------------------------------------
        # Try extracting JSON object
        # ----------------------------------------------

        try:

            start = text.find("{")

            end = text.rfind("}")

            if start != -1 and end != -1:

                return json.loads(

                    text[start:end + 1]

                )

        except Exception:

            pass

        # ----------------------------------------------
        # Try extracting JSON array
        # ----------------------------------------------

        try:

            start = text.find("[")

            end = text.rfind("]")

            if start != -1 and end != -1:

                return json.loads(

                    text[start:end + 1]

                )

        except Exception:

            pass

        cls.logger.info(
            "Response is not JSON."
        )

        return None

    # ------------------------------------------------------
    # Is JSON
    # ------------------------------------------------------

    @classmethod
    def is_json(
        cls,
        text,
    ):

        return cls._try_json(text) is not None

    # ------------------------------------------------------
    # Parse JSON
    # ------------------------------------------------------

    @classmethod
    def parse_json(
        cls,
        text,
    ):

        parsed = cls._try_json(text)

        if parsed is None:

            raise ValueError(
                "Invalid JSON response."
            )

        return parsed