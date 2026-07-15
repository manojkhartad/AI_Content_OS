# ==========================================================
# Imports
# ==========================================================

import hashlib
import json
from pathlib import Path
from typing import Optional


# ==========================================================
# Cache Directory
# ==========================================================

CACHE_DIR = Path("cache")

CACHE_DIR.mkdir(

    parents=True,

    exist_ok=True

)

CACHE_FILE = CACHE_DIR / "prompt_cache.json"


# ==========================================================
# Prompt Cache
# ==========================================================

class PromptCache:

    def __init__(self):

        self.cache = {}

        self.cache_hits = 0

        self.cache_misses = 0

        self._load()

    # ------------------------------------------------------
    # Load Cache
    # ------------------------------------------------------

    def _load(self):

        if not CACHE_FILE.exists():

            self.cache = {}

            return

        try:

            with open(

                CACHE_FILE,

                "r",

                encoding="utf-8"

            ) as file:

                self.cache = json.load(file)

        except Exception:

            self.cache = {}

    # ------------------------------------------------------
    # Save Cache
    # ------------------------------------------------------

    def _save(self):

        with open(

            CACHE_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.cache,

                file,

                indent=4,

                ensure_ascii=False

            )

    # ------------------------------------------------------
    # Hash Prompt
    # ------------------------------------------------------

    @staticmethod
    def _hash(prompt: str) -> str:

        return hashlib.sha256(

            prompt.encode("utf-8")

        ).hexdigest()

    # ------------------------------------------------------
    # Get
    # ------------------------------------------------------

    def get(

        self,

        prompt: str

    ) -> Optional[str]:

        key = self._hash(prompt)

        if key in self.cache:

            self.cache_hits += 1

            print("\n✓ Prompt Cache Hit")

            return self.cache[key]

        self.cache_misses += 1

        print("\nPrompt Cache Miss")

        return None

    # ------------------------------------------------------
    # Set
    # ------------------------------------------------------

    def set(

        self,

        prompt: str,

        response: str

    ):

        key = self._hash(prompt)

        self.cache[key] = response

        self._save()

    # ------------------------------------------------------
    # Clear
    # ------------------------------------------------------

    def clear(self):

        self.cache = {}

        self.cache_hits = 0

        self.cache_misses = 0

        self._save()

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    def stats(self):

        print("\n===================================")

        print("Prompt Cache")

        print("===================================")

        print(

            f"Entries : {len(self.cache)}"

        )

        print(

            f"Hits    : {self.cache_hits}"

        )

        print(

            f"Misses  : {self.cache_misses}"

        )

        print("===================================")


# ==========================================================
# Singleton
# ==========================================================

prompt_cache = PromptCache()