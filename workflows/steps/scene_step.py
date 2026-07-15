from agents.agent_manager import AgentManager

from exporters.scene_exporter import SceneExporter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class SceneStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Scene Generation ==========")

        agent = AgentManager().get("scene")

        scene_list = agent.generate_scenes(
            context.get("draft"),
            context.get("character_bibles")
        )

        SceneExporter.export(
            scene_list
        )

        context.set(
            "scene_list",
            scene_list
        )

        return context