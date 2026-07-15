from agents.agent_manager import AgentManager

from formatters.story_formatter import StoryFormatter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class VideoStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Video Generation ==========")

        agent = AgentManager().get("video_generation")

        generated_video = agent.generate_video(
            draft=context.get("draft"),
            generated_images=context.get("generated_images"),
            generated_audio=context.get("generated_audio")
        )

        StoryFormatter.print_story(
            context.get("draft")
        )

        print("\n===================================")
        print("AI Content OS Completed")
        print("===================================")
        print(f"Final Video : {generated_video.video_path}")

        context.set(
            "generated_video",
            generated_video
        )

        return context