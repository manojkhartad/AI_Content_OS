from agents.base_llm_agent import BaseLLMAgent

from models.research_report import ResearchReport

from prompts.research.story_prompt import StoryPrompt


class ResearchAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Research Agent")

    def research(self, topic):

        return self.run(topic)

    def run(self, topic):

        self.start()

        print(f"Research Started on: {topic}")

        prompt = StoryPrompt()

        final_prompt = prompt.build(topic)

        research_text = self.think(final_prompt)

        return ResearchReport(
            topic=topic,
            content_type="Kids Story",
            target_audience="5-8 Years",
            goal="Educational + Fun",
            tone="Funny",
            research=research_text
        )