# ==========================================================
# Imports
# ==========================================================

from workflows.base_workflow import BaseWorkflow
from workflows.workflow_context import WorkflowContext
from workflows.workflow_result import WorkflowResult

from workflows.steps.research_step import ResearchStep
from workflows.steps.character_step import CharacterStep
from workflows.steps.character_bible_step import CharacterBibleStep
from workflows.steps.writer_step import WriterStep
from workflows.steps.reviewer_step import ReviewerStep
from workflows.steps.scene_step import SceneStep
from workflows.steps.narration_step import NarrationStep
from workflows.steps.image_prompt_step import ImagePromptStep
from workflows.steps.image_generation_step import ImageGenerationStep
from workflows.steps.tts_step import TTSStep
from workflows.steps.video_step import VideoStep

from utils.checkpoint_manager import CheckpointManager


# ==========================================================
# Story Workflow
# ==========================================================

class StoryWorkflow(BaseWorkflow):

    def __init__(self):

        self.steps = [

            ResearchStep(),

            CharacterStep(),

            CharacterBibleStep(),

            WriterStep(),

            ReviewerStep(),

            SceneStep(),

            NarrationStep(),

            ImagePromptStep(),

            ImageGenerationStep(),

            TTSStep(),

            VideoStep(),

        ]

        self.checkpoint = CheckpointManager()

    # ------------------------------------------------------
    # Run Workflow
    # ------------------------------------------------------

    def run(

        self,

        context: WorkflowContext

    ) -> WorkflowResult:

        print("\n===================================")
        print("Story Workflow Started")
        print("===================================")

        completed_steps = self.checkpoint.load()

        for step in self.steps:

            step_name = step.__class__.__name__

            # --------------------------------------------------
            # Resume Support
            # --------------------------------------------------

            if step_name in completed_steps:

                print(
                    f"\n✓ Skipping {step_name}"
                )

                continue

            print(
                f"\n========== {step_name} =========="
            )

            context.profiler.start(step_name)

            try:

                context = step.execute(context)

                self.checkpoint.save(step_name)

            except Exception as e:

                print(
                    f"\n❌ {step_name} Failed"
                )

                print(e)

                raise

            finally:

                context.profiler.stop(step_name)

        print("\n==============================")
        print("Story Generated Successfully")
        print("==============================")

        context.profiler.report()

        self.checkpoint.clear()

        return WorkflowResult(

            story=context.get("draft"),

            scenes=context.get("scene_list"),

            narrations=context.get("narration_list"),

            images=context.get("generated_images"),

            audio=context.get("generated_audio"),

            video=context.get("generated_video"),

        )