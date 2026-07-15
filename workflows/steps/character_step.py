from agents.agent_manager import AgentManager

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class CharacterStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Character Generation ==========")

        agent = AgentManager().get("character")

        characters = agent.generate_characters(
            context.get("research_report")
        )

        context.set(
            "characters",
            characters
        )

        return context