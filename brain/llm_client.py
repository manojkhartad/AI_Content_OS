from google import genai

from config.settings import GEMINI_API_KEY
from brain.model_registry import ModelRegistry
from brain.retry_manager import RetryManager
from brain.fallback_manager import FallbackManager
from brain.response_parser import ResponseParser
from brain.usage_tracker import UsageTracker
from brain.exceptions import LLMGenerationError


class LLMClient:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.models = ModelRegistry.get_models()
        self.usage_tracker = UsageTracker()

    def generate(self, prompt):

        last_error = None

        models = FallbackManager.get_models(self.models)

        for model in models:

            start_time = self.usage_tracker.start_request(model)

            try:

                print(f"\nTrying Model : {model}")

                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                self.usage_tracker.end_request(start_time, success=True)

                print(f"Success : {model}")

                return ResponseParser.parse(response)

            except Exception as e:

                self.usage_tracker.end_request(start_time, success=False)

                if RetryManager.should_retry(e):

                    print(f"Failed : {model}")
                    print(e)

                    last_error = e
                    continue

                raise

        raise LLMGenerationError(
            f"All models failed to generate a response. Last error: {last_error}"
        )