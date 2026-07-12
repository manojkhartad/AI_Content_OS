import json


def parse_json(response: str) -> dict:
    """
    Parse JSON returned by the LLM.

    Supports:
    - Plain JSON
    - ```json ... ```
    - ``` ... ```

    Returns:
        dict

    Raises:
        ValueError if JSON is invalid.
    """

    if not response:
        raise ValueError("LLM returned an empty response.")

    cleaned = response.strip()

    # Remove ```json
    if cleaned.startswith("```json"):
        cleaned = cleaned.replace("```json", "", 1)

    # Remove ```
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