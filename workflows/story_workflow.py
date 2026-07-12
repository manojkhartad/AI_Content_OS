from agents.research_agent import ResearchAgent
from agents.character_agent import CharacterAgent
from agents.character_bible_agent import CharacterBibleAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from formatters.story_formatter import StoryFormatter

from production.story_exporter import StoryExporter
from production.character_bible_exporter import CharacterBibleExporter


class StoryWorkflow:

    def run(self, topic):

        print("Story Workflow Started")

        # -----------------------------
        # Research
        # -----------------------------

        research_agent = ResearchAgent()
        research_agent.start()

        research_report = research_agent.research(topic)

        # -----------------------------
        # Character Profiles
        # -----------------------------

        character_agent = CharacterAgent()
        character_agent.start()

        characters = character_agent.generate_characters(
            research_report
        )

        # -----------------------------
        # Character Bible
        # -----------------------------

        character_bible_agent = CharacterBibleAgent()
        character_bible_agent.start()

        character_bibles = character_bible_agent.generate_character_bibles(
            characters
        )

        # -----------------------------
        # Export Character Bibles
        # -----------------------------

        CharacterBibleExporter.export(
            character_bibles
        )

        # -----------------------------
        # Story Writer
        # -----------------------------

        writer_agent = WriterAgent()
        writer_agent.start()

        draft = writer_agent.write(
            research_report,
            character_bibles
        )

        # -----------------------------
        # Story Reviewer
        # -----------------------------

        reviewer_agent = ReviewerAgent()
        reviewer_agent.start()

        review = reviewer_agent.review(draft)

        StoryFormatter.print_review(review)

        # -----------------------------
        # Export Story
        # -----------------------------

        exporter = StoryExporter()
        exporter.export(draft)

        StoryFormatter.print_story(draft)

        return draft