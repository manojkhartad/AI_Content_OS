from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from production.story_exporter import StoryExporter


class StoryWorkflow:

    def run(self, topic):

        print("Story Workflow Started")

        # Step 1 : Research

        research_agent = ResearchAgent()
        research_agent.start()

        research_report = research_agent.research(topic)

        # Step 2 : Writing

        writer_agent = WriterAgent()
        writer_agent.start()

        story_draft = writer_agent.write(research_report)

        # Step 3 : Review

        reviewer_agent = ReviewerAgent()
        reviewer_agent.start()

        review = reviewer_agent.review(story_draft)

        print("\n==============================")
        print("Story Review")
        print("==============================")
        print(f"Score : {review.score}/100")
        print(f"Passed : {'Yes' if review.score >= 85 else 'No'}")
        print("\nFeedback:")
        print(review.feedback)

        # Step 4 : Export

        exporter = StoryExporter()
        exporter.export(story_draft)

        return story_draft