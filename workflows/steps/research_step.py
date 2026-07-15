from agents.agent_manager import AgentManager

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class ResearchStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Research ==========")

        agent = AgentManager().get("research")

        research_report = agent.research(
            context.topic
        )

        context.set(
            "research_report",
            research_report
        )

        return context