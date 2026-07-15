from agents.base_llm_agent import BaseLLMAgent

from models.story_draft import StoryDraft

from prompts.writing.writer_prompt import WriterPrompt

from utils.json_parser import parse_json


class WriterAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Writer Agent")

    def write(
        self,
        research_report,
        character_bibles
    ):

        return self.run(
            research_report,
            character_bibles
        )

    def run(
        self,
        research_report,
        character_bibles
    ):

        self.start()

        print("Story Writing Started")

        prompt = WriterPrompt.generate(
            research_report,
            character_bibles
        )

        response = self.think(prompt)

        data = parse_json(response)

        return StoryDraft(

            title=data.get("title", ""),

            story=data.get("story", ""),

            moral=data.get("moral", ""),

            word_count=data.get("word_count", 0)

        )