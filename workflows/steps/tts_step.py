from agents.agent_manager import AgentManager

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class TTSStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Audio Generation ==========")

        agent = AgentManager().get("tts")

        generated_audio = agent.generate_audio(
            context.get("narration_list")
        )

        context.set(
            "generated_audio",
            generated_audio
        )

        return context