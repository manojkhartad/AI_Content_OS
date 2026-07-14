from brain.llm_router import LLMRouter


class Brain:

    def __init__(self):
        self.router = LLMRouter()

    def think(self, prompt):

        print("Brain Thinking...")

        return self.router.generate(prompt)