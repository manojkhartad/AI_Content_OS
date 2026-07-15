from agents.agent_manager import AgentManager

from formatters.story_formatter import StoryFormatter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class ReviewerStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Story Review ==========")

        agent = AgentManager().get("reviewer")

        review = agent.review(
            context.get("draft")
        )

        StoryFormatter.print_review(
            review
        )

        context.set(
            "review",
            review
        )

        return context