from agents.agent_manager import AgentManager

from exporters.narration_exporter import NarrationExporter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class NarrationStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Narration Generation ==========")

        agent = AgentManager().get("narration")

        narration_list = agent.generate_narrations(
            context.get("scene_list")
        )

        NarrationExporter.export(
            narration_list
        )

        context.set(
            "narration_list",
            narration_list
        )

        return context