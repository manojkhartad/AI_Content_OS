from agents.agent_manager import AgentManager

from exporters.image_prompt_exporter import ImagePromptExporter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class ImagePromptStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Image Prompt Generation ==========")

        agent = AgentManager().get("image_prompt")

        image_prompts = agent.generate_image_prompts(
            context.get("scene_list").scenes,
            context.get("character_bibles")
        )

        ImagePromptExporter.export(
            image_prompts
        )

        context.set(
            "image_prompts",
            image_prompts
        )

        return context