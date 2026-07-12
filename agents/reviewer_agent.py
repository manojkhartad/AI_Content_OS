from agents.base_agent import BaseAgent

from brain.brain import Brain

from prompts.reviewing.reviewer_prompt import ReviewerPrompt

from models.review_report import ReviewReport

from utils.json_parser import parse_json


class ReviewerAgent(BaseAgent):

    def __init__(self):
        super().__init__("Reviewer Agent")

    def review(self, story):

        print("Story Review Started")

        prompt = ReviewerPrompt().build(story)

        brain = Brain()

        response = brain.think(prompt)

        data = parse_json(response)

        report = ReviewReport(
            passed=data["passed"],
            score=data["score"],
            feedback=data["feedback"]
        )

        return report