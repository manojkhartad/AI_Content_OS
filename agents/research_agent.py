from agents.base_agent import BaseAgent

from models.research_report import ResearchReport

from brain.brain import Brain

from prompts.research.story_prompt import StoryPrompt


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("Research Agent")

    def research(self, topic):

        print(f"Research Started on: {topic}")

        prompt = StoryPrompt()

        final_prompt = prompt.build(topic)

        brain = Brain()

        research_text = brain.think(final_prompt)

        report = ResearchReport(
            topic=topic,
            content_type="Kids Story",
            target_audience="5-8 Years",
            goal="Educational + Fun",
            tone="Funny",
            research=research_text
        )

        return report