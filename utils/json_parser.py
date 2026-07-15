import json


def parse_json(response) -> dict:
    """
    Parse JSON returned by the LLM.

    Supports:
    - dict (already parsed)
    - list (already parsed)
    - Plain JSON string
    - ```json ... ```
    - ``` ... ```
    """

    if response is None:
        raise ValueError("LLM returned an empty response.")

    # Already parsed
    if isinstance(response, (dict, list)):
        return response

    if not isinstance(response, str):
        raise TypeError(
            f"Expected str, dict or list. Got {type(response).__name__}."
        )

    cleaned = response.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned.replace("```json", "", 1)

    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```", "", 1)

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON returned by LLM.\n\nResponse:\n{response}"
        ) from e