import json


class WriterPrompt:

    def build(self, report):

        schema = {
            "title": "Story title",
            "story": "Complete children's story",
            "moral": "Moral of the story"
        }

        return f"""
You are an expert children's story writer.

Your job is to write a beautiful children's story using the research provided below.

Research:

{report.research}

Topic:
{report.topic}

Target Audience:
{report.target_audience}

Goal:
{report.goal}

Tone:
{report.tone}

Instructions:

- Write in simple English.
- Use short and easy sentences.
- Make the story fun and engaging.
- Give each character a unique personality.
- Include natural dialogues where appropriate.
- Story length should be around 500 words.
- End with a happy ending.
- Include a clear moral lesson.

Return ONLY valid JSON.

Do NOT write explanations.
Do NOT use markdown.
Do NOT wrap JSON inside ```json blocks.

JSON Format:

{json.dumps(schema, indent=4)}
"""