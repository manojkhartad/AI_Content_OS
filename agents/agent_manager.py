from agents.base_agent import BaseAgent
from agents.agent_factory import AgentFactory


class AgentManager(BaseAgent):

    _instances = {}

    def __init__(self):
        super().__init__("Agent Manager")

    def get(self, name: str):

        if name not in self._instances:

            self._instances[name] = (
                AgentFactory.create(name)
            )

        return self._instances[name]

    def run(self, *args, **kwargs):
        self.start()