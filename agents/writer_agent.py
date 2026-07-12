from agents.base_agent import BaseAgent
from brain.brain import Brain

from prompts.writing.writer_prompt import WriterPrompt

from models.story_draft import StoryDraft

from utils.json_parser import parse_json


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__("Writer Agent")

    def write(self, report):

        print("Story Writing Started")

        prompt = WriterPrompt()

        final_prompt = prompt.build(report)

        brain = Brain()

        response = brain.think(final_prompt)

        data = parse_json(response)

        story = StoryDraft(
            title=data["title"],
            story=data["story"],
            moral=data["moral"],
            word_count=len(data["story"].split())
        )

        return story