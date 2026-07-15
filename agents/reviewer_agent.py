from agents.base_llm_agent import BaseLLMAgent

from prompts.reviewing.reviewer_prompt import ReviewerPrompt

from models.review_report import ReviewReport

from utils.json_parser import parse_json


class ReviewerAgent(BaseLLMAgent):

    def __init__(self):
        super().__init__("Reviewer Agent")

    def review(self, story):

        return self.run(story)

    def run(self, story):

        self.start()

        print("Story Review Started")

        prompt = ReviewerPrompt().build(story)

        response = self.think(prompt)

        data = parse_json(response)

        return ReviewReport(
            passed=data["passed"],
            score=data["score"],
            feedback=data["feedback"]
        )