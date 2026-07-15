from agents.agent_manager import AgentManager

from exporters.story_exporter import StoryExporter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class WriterStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Story Writing ==========")

        agent = AgentManager().get("writer")

        draft = agent.write(
            context.get("research_report"),
            context.get("character_bibles")
        )

        StoryExporter.export(
            draft
        )

        context.set(
            "draft",
            draft
        )

        return context