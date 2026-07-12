from agents.base_agent import BaseAgent

from brain.brain import Brain

from models.story_draft import StoryDraft

from prompts.writing.writer_prompt import WriterPrompt

from utils.json_parser import parse_json


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__("Writer Agent")

    def write(self, research_report, character_bibles):

        print("Story Writing Started")

        prompt = WriterPrompt.generate(
            research_report,
            character_bibles
        )

        brain = Brain()

        response = brain.think(prompt)

        data = parse_json(response)

        return StoryDraft(

            title=data.get("title", ""),

            story=data.get("story", ""),

            moral=data.get("moral", ""),

            word_count=data.get("word_count", 0)

        )