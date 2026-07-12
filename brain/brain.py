from brain.llm_client import LLMClient


class Brain:

    def think(self, prompt):

        print("Brain Thinking...")

        llm = LLMClient()

        response = llm.generate(prompt)

        return response