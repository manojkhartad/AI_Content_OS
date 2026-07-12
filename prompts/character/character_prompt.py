class CharacterPrompt:

    @staticmethod
    def generate(research_report):

        return f"""
You are an expert story planner.

Your job is to identify the characters required for the story.

Project Information

Topic:
{research_report.topic}

Content Type:
{research_report.content_type}

Target Audience:
{research_report.target_audience}

Goal:
{research_report.goal}

Tone:
{research_report.tone}

Instructions:

- Identify only the characters needed.
- Do NOT write the story.
- Do NOT invent detailed personalities.
- Do NOT invent relationships.
- Keep descriptions short (1 sentence).
- Create between 2 and 5 characters.

Role must be one of:

- Main Character
- Supporting Character
- Antagonist
- Mentor
- Narrator

Return ONLY valid JSON.

Example:

{{
    "characters": [
        {{
            "name": "Leo",
            "role": "Main Character",
            "species": "Lion",
            "description": "A proud lion who believes he is the king of the forest."
        }},
        {{
            "name": "Barnaby",
            "role": "Supporting Character",
            "species": "Rabbit",
            "description": "A clever rabbit who solves problems using intelligence."
        }}
    ]
}}
"""