from agents.research_agent import ResearchAgent


class StoryWorkflow:

    def run(self, topic):
        print("Story Workflow Started")

        research_agent = ResearchAgent()
        research_agent.start()

        report = research_agent.research(topic)

        return report