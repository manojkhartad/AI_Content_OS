class ReviewerPrompt:

    def build(self, story):

        return f"""
You are a professional children's story reviewer.

Your job is to review the story and return ONLY valid JSON.

Review the story using the following criteria:

1. Suitable for children aged 5-8.
2. Easy English.
3. Clear beginning, middle and ending.
4. Fun and engaging.
5. Positive moral.
6. No scary, violent or inappropriate content.
7. Grammar and spelling are correct.
8. Story length should be around 400-600 words.

Story Title:
{story.title}

Story:
{story.story}

Moral:
{story.moral}

Return ONLY this JSON:

{{
    "passed": true,
    "score": 95,
    "feedback": "Short explanation of the review."
}}

Do not write markdown.

Do not write explanations.

Return only JSON.
"""