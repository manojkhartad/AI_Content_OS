from prompts.research.base_prompt import BasePrompt


class StoryPrompt(BasePrompt):

    def __init__(self):

        super().__init__(
            content_type="Kids Story",
            target_audience="5-8 Years",
            goal="Educational + Fun",
            tone="Funny"
        )

    def build(self, topic):

        return f"""
Research this topic for a kids educational story.

Topic:
{topic}

Instructions:

- Write in simple English.
- Target audience: {self.target_audience}
- Goal: {self.goal}
- Tone: {self.tone}
- Reply in only 5-6 short sentences.
"""