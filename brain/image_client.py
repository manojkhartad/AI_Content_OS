# ==========================================================
# Imports
# ==========================================================

import threading
import time
from pathlib import Path
from urllib.parse import quote

import requests

from config.settings import (
    IMAGE_PROVIDER,
    IMAGE_MODEL,
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    IMAGE_TIMEOUT,
    IMAGE_MAX_RETRIES,
    IMAGE_RETRY_DELAYS,
)


# ==========================================================
# Image Client
# ==========================================================

class ImageClient:

    POLLINATIONS_URL = "https://image.pollinations.ai/prompt/"

    _session = requests.Session()

    _session.headers.update(
        {
            "User-Agent": "AI-Content-OS/1.0"
        }
    )

    # ------------------------------------------------------
    # Rate Limiter
    # ------------------------------------------------------

    _lock = threading.Lock()

    _last_request_time = 0.0

    MIN_REQUEST_INTERVAL = 2.0

    # ------------------------------------------------------
    # Build Pollinations URL
    # ------------------------------------------------------

    @classmethod
    def _build_pollinations_url(
        cls,
        prompt: str,
        width: int,
        height: int,
    ):

        encoded_prompt = quote(prompt)

        return (
            f"{cls.POLLINATIONS_URL}"
            f"{encoded_prompt}"
            f"?width={width}"
            f"&height={height}"
            f"&model={IMAGE_MODEL}"
        )

    # ------------------------------------------------------
    # Rate Limiter
    # ------------------------------------------------------

    @classmethod
    def _wait_for_rate_limit(cls):

        with cls._lock:

            now = time.time()

            elapsed = now - cls._last_request_time

            if elapsed < cls.MIN_REQUEST_INTERVAL:

                wait = cls.MIN_REQUEST_INTERVAL - elapsed

                print(
                    f"Rate Limit : Waiting {wait:.1f} sec..."
                )

                time.sleep(wait)

            cls._last_request_time = time.time()

    # ------------------------------------------------------
    # Generate Image
    # ------------------------------------------------------

    @classmethod
    def generate_image(
        cls,
        prompt: str,
        output_path: Path,
        width: int = IMAGE_WIDTH,
        height: int = IMAGE_HEIGHT,
    ) -> Path:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if IMAGE_PROVIDER != "pollinations":

            raise NotImplementedError(
                f"{IMAGE_PROVIDER} provider is not implemented."
            )

        image_url = cls._build_pollinations_url(
            prompt,
            width,
            height,
        )

        last_error = None

        for attempt in range(IMAGE_MAX_RETRIES):

            try:

                print(
                    f"\nGenerating Image "
                    f"(Attempt {attempt + 1}/{IMAGE_MAX_RETRIES})..."
                )

                cls._wait_for_rate_limit()

                response = cls._session.get(
                    image_url,
                    timeout=IMAGE_TIMEOUT,
                    stream=True,
                )

                response.raise_for_status()

                with open(output_path, "wb") as file:

                    for chunk in response.iter_content(
                        chunk_size=8192
                    ):

                        if chunk:

                            file.write(chunk)

                print(
                    f"Image Saved : {output_path}"
                )

                return output_path

            except requests.exceptions.HTTPError as error:

                last_error = error

                status = error.response.status_code

                print(
                    f"\nHTTP Error : {status}"
                )

                if (
                    status in (
                        429,
                        500,
                        502,
                        503,
                        504,
                    )
                    and attempt < IMAGE_MAX_RETRIES - 1
                ):

                    delay = IMAGE_RETRY_DELAYS[
                        min(
                            attempt,
                            len(IMAGE_RETRY_DELAYS) - 1,
                        )
                    ]

                    print(
                        f"Retrying in {delay} sec..."
                    )

                    time.sleep(delay)

                    continue

                raise

            except (
                requests.exceptions.Timeout,
                requests.exceptions.ConnectionError,
                requests.exceptions.RequestException,
            ) as error:

                last_error = error

                print(
                    f"\nNetwork Error : {error}"
                )

                if attempt < IMAGE_MAX_RETRIES - 1:

                    delay = IMAGE_RETRY_DELAYS[
                        min(
                            attempt,
                            len(IMAGE_RETRY_DELAYS) - 1,
                        )
                    ]

                    print(
                        f"Retrying in {delay} sec..."
                    )

                    time.sleep(delay)

                    continue

                raise

            except Exception as error:

                last_error = error

                print(
                    f"\nUnexpected Error : {error}"
                )

                if attempt < IMAGE_MAX_RETRIES - 1:

                    delay = IMAGE_RETRY_DELAYS[
                        min(
                            attempt,
                            len(IMAGE_RETRY_DELAYS) - 1,
                        )
                    ]

                    print(
                        f"Retrying in {delay} sec..."
                    )

                    time.sleep(delay)

                    continue

                raise

        raise RuntimeError(
            f"Image generation failed.\n{last_error}"
        )