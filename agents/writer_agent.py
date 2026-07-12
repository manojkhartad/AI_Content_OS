from agents.base_agent import BaseAgent

from brain.brain import Brain

from models.story_draft import StoryDraft

from prompts.writing.writer_prompt import WriterPrompt

from utils.json_parser import parse_json


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__("Writer Agent")

    def write(self, research_report, characters):

        print("Story Writing Started")

        prompt = WriterPrompt.generate(
            research_report,
            characters
        )

        brain = Brain()

        response = brain.think(prompt)

        data = parse_json(response)

        draft = StoryDraft(
            title=data["title"],
            story=data["story"],
            moral=data["moral"],
            word_count=data["word_count"]
        )

        return draft