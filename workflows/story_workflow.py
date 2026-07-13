from agents.research_agent import ResearchAgent
from agents.character_agent import CharacterAgent
from agents.character_bible_agent import CharacterBibleAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent
from agents.scene_agent import SceneAgent
from agents.narration_agent import NarrationAgent
from agents.image_prompt_agent import ImagePromptAgent
from agents.image_generation_agent import ImageGenerationAgent
from agents.tts_agent import TTSAgent
from agents.video_generation_agent import VideoGenerationAgent

from formatters.story_formatter import StoryFormatter

from exporters.story_exporter import StoryExporter
from exporters.character_bible_exporter import CharacterBibleExporter
from exporters.scene_exporter import SceneExporter
from exporters.narration_exporter import NarrationExporter
from exporters.image_prompt_exporter import ImagePromptExporter


class StoryWorkflow:

    def run(self, topic):

        print("Story Workflow Started")

        # --------------------------------------------------
        # Research
        # --------------------------------------------------

        research_agent = ResearchAgent()
        research_agent.start()

        research_report = research_agent.research(topic)

        # --------------------------------------------------
        # Character Profiles
        # --------------------------------------------------

        character_agent = CharacterAgent()
        character_agent.start()

        characters = character_agent.generate_characters(
            research_report
        )

        # --------------------------------------------------
        # Character Bible
        # --------------------------------------------------

        character_bible_agent = CharacterBibleAgent()
        character_bible_agent.start()

        character_bibles = (
            character_bible_agent.generate_character_bibles(
                characters
            )
        )

        # --------------------------------------------------
        # Export Character Bibles
        # --------------------------------------------------

        CharacterBibleExporter.export(
            character_bibles
        )

        # --------------------------------------------------
        # Story Writer
        # --------------------------------------------------

        writer_agent = WriterAgent()
        writer_agent.start()

        draft = writer_agent.write(
            research_report,
            character_bibles
        )

        # --------------------------------------------------
        # Story Reviewer
        # --------------------------------------------------

        reviewer_agent = ReviewerAgent()
        reviewer_agent.start()

        review = reviewer_agent.review(
            draft
        )

        StoryFormatter.print_review(
            review
        )

        # --------------------------------------------------
        # Export Story
        # --------------------------------------------------

        StoryExporter.export(
            draft
        )

        # --------------------------------------------------
        # Scene Generation
        # --------------------------------------------------

        scene_agent = SceneAgent()
        scene_agent.start()

        scene_list = scene_agent.generate_scenes(
            draft,
            character_bibles
        )

        # --------------------------------------------------
        # Export Scenes
        # --------------------------------------------------

        SceneExporter.export(
            scene_list
        )

        # --------------------------------------------------
        # Narration Generation
        # --------------------------------------------------

        narration_agent = NarrationAgent()
        narration_agent.start()

        narration_list = (
            narration_agent.generate_narrations(
                scene_list
            )
        )

        # --------------------------------------------------
        # Export Narrations
        # --------------------------------------------------

        NarrationExporter.export(
            narration_list
        )

        # --------------------------------------------------
        # Image Prompt Generation
        # --------------------------------------------------

        image_prompt_agent = ImagePromptAgent()
        image_prompt_agent.start()

        image_prompts = (
            image_prompt_agent.generate_image_prompts(
                scene_list.scenes,
                character_bibles
            )
        )

        # --------------------------------------------------
        # Export Image Prompts
        # --------------------------------------------------

        ImagePromptExporter.export(
            image_prompts
        )

        # --------------------------------------------------
        # Image Generation
        # --------------------------------------------------

        image_generation_agent = ImageGenerationAgent()
        image_generation_agent.start()

        generated_images = (
            image_generation_agent.generate_images(
                image_prompts
            )
        )

        # --------------------------------------------------
        # Audio Generation (TTS)
        # --------------------------------------------------

        tts_agent = TTSAgent()
        tts_agent.start()

        generated_audio = (
            tts_agent.generate_audio(
                narration_list
            )
        )

        # --------------------------------------------------
        # Video Generation
        # --------------------------------------------------

        video_generation_agent = VideoGenerationAgent()
        video_generation_agent.start()

        generated_video = (
            video_generation_agent.generate_video(
                draft=draft,
                generated_images=generated_images,
                generated_audio=generated_audio
            )
        )

        # --------------------------------------------------
        # Print Story
        # --------------------------------------------------

        StoryFormatter.print_story(
            draft
        )

        print("\n===================================")
        print("AI Content OS Completed")
        print("===================================")
        print(f"Final Video : {generated_video.video_path}")

        return {
            "story": draft,
            "scenes": scene_list,
            "narrations": narration_list,
            "images": generated_images,
            "audio": generated_audio,
            "video": generated_video,
        }