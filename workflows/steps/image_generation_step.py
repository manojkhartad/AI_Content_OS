from agents.agent_manager import AgentManager

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class ImageGenerationStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Image Generation ==========")

        agent = AgentManager().get("image_generation")

        generated_images = agent.generate_images(
            context.get("image_prompts")
        )

        context.set(
            "generated_images",
            generated_images
        )

        return context