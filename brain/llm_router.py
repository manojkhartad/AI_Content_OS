from brain.llm_client import LLMClient


class LLMRouter:

    def __init__(self):
        self.client = LLMClient()

    def generate(self, prompt):

        return self.client.generate(prompt)