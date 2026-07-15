from agents.agent_registry import AGENT_REGISTRY


class AgentFactory:

    @staticmethod
    def create(name: str):

        if name not in AGENT_REGISTRY:
            raise ValueError(
                f"Unknown agent: {name}"
            )

        return AGENT_REGISTRY[name]()