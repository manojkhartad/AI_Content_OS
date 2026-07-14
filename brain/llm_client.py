from google import genai
from google.genai.errors import ClientError, ServerError

from config.settings import GEMINI_API_KEY
from brain.model_registry import ModelRegistry


class LLMClient:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.models = ModelRegistry.get_models()

    def generate(self, prompt):

        last_error = None

        for model in self.models:

            try:

                print(f"\nTrying Model : {model}")

                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                print(f"Success : {model}")

                return response.text

            except (ClientError, ServerError) as e:

                print(f"Failed : {model}")
                print(e)

                last_error = e

        raise last_error