class WriterPrompt:

    @staticmethod
    def generate(research_report, characters):

        character_section = ""

        for character in characters:
            character_section += f"""
Name: {character.name}
Role: {character.role}
Species: {character.species}
Description: {character.description}

"""

        return f"""
You are an expert children's story writer.

Write an original educational story.

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

Characters

{character_section}

Story Requirements

- Use ONLY the characters listed above.
- Keep the story between 350 and 450 words.
- Use simple English suitable for children aged 5–8.
- Give the story a clear beginning, middle and ending.
- Make the story fun, educational and engaging.
- End with a positive moral.
- Do not introduce new major characters unless absolutely necessary.
- Do not include violence, horror or inappropriate content.

Return ONLY valid JSON.

JSON Schema

{{
    "title": "",
    "story": "",
    "moral": "",
    "word_count": 0
}}
"""