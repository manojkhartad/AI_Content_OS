# ==========================================================
# Imports
# ==========================================================

from agents.research_agent import ResearchAgent
from agents.character_agent import CharacterAgent
from agents.character_bible_agent import CharacterBibleAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from exporters.story_exporter import StoryExporter
from exporters.character_bible_exporter import CharacterBibleExporter

from formatters.story_formatter import StoryFormatter


# ==========================================================
# Story Workflow
# ==========================================================

class StoryWorkflow:

    def run(self, topic):

        print("Story Workflow Started")

        # ==================================================
        # Step 1 : Research
        # ==================================================

        research_agent = ResearchAgent()
        research_agent.start()

        research_report = research_agent.research(topic)

        # ==================================================
        # Step 2 : Character Profiles
        # ==================================================

        character_agent = CharacterAgent()
        character_agent.start()

        characters = character_agent.generate_characters(
            research_report
        )

        # ==================================================
        # Step 3 : Character Bibles
        # ==================================================

        character_bible_agent = CharacterBibleAgent()
        character_bible_agent.start()

        character_bibles = (
            character_bible_agent.generate_character_bibles(
                characters
            )
        )

        CharacterBibleExporter.export(
            character_bibles
        )

        # ==================================================
        # Step 4 : Story Writing
        # ==================================================

        writer_agent = WriterAgent()
        writer_agent.start()

        story = writer_agent.write(
            research_report,
            character_bibles
        )

        # ==================================================
        # Step 5 : Story Review
        # ==================================================

        reviewer_agent = ReviewerAgent()
        reviewer_agent.start()

        review = reviewer_agent.review(
            story
        )

        StoryFormatter.print_review(
            review
        )

        # ==================================================
        # Step 6 : Story Export
        # ==================================================

        StoryExporter.export(
            story
        )

        StoryFormatter.print_story(
            story
        )

        return story