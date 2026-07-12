from agents.base_agent import BaseAgent
from models.research_report import ResearchReport
from brain.brain import Brain

class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("Research Agent")

    def research(self, topic):
        print(f"Research Started on: {topic}")

        brain = Brain()
        brain_data = brain.think(topic)

        report = ResearchReport(
            topic=topic,
            content_type="Kids Story",
            target_audience=brain_data["target_audience"],
            goal=brain_data["goal"],
            tone=brain_data["tone"]
        )

        return report