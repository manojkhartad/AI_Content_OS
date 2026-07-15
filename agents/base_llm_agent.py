from agents.base_agent import BaseAgent
from brain.brain import Brain


class BaseLLMAgent(BaseAgent):

    def __init__(self, name: str):
        super().__init__(name)

        self.brain = Brain()

    def think(self, prompt: str):

        return self.brain.think(prompt)

    def run(self, *args, **kwargs):
        raise NotImplementedError(
            "LLM agents must implement run method"
        )