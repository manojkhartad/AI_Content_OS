from agents.research_agent import ResearchAgent
from agents.character_agent import CharacterAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from formatters.story_formatter import StoryFormatter
from production.story_exporter import StoryExporter


class StoryWorkflow:

    def run(self, topic):

        print("Story Workflow Started")

        # Research

        research_agent = ResearchAgent()
        research_agent.start()

        research_report = research_agent.research(topic)

        # Characters

        character_agent = CharacterAgent()
        character_agent.start()

        characters = character_agent.generate_characters(
            research_report
        )

        # Writer

        writer_agent = WriterAgent()
        writer_agent.start()

        draft = writer_agent.write(
            research_report,
            characters
        )

        # Reviewer

        reviewer_agent = ReviewerAgent()
        reviewer_agent.start()

        review = reviewer_agent.review(draft)

        StoryFormatter.print_review(review)

        StoryExporter.export(draft)

        StoryFormatter.print_story(draft)

        return draft