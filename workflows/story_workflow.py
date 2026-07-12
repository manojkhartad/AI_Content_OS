from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent


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

        return story_draft