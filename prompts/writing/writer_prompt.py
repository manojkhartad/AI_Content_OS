class WriterPrompt:

    @staticmethod
    def generate(research_report, character_bibles):

        characters = ""

        for character in character_bibles:

            characters += f"""

Name:
{character.name}

Species:
{character.species}

Role:
{character.role}

Appearance:
{character.appearance}

Clothing:
{character.clothing}

Accessories:
{character.accessories}

Personality:
{character.personality}

Strengths:
{character.strengths}

Weaknesses:
{character.weaknesses}

Goals:
{character.goals}

Voice Style:
{character.voice_style}

Catch Phrase:
{character.catch_phrase}

Movement Style:
{character.movement_style}

Default Expression:
{character.default_expression}

Default Pose:
{character.default_pose}

Gestures:
{character.gestures}

----------------------------------------
"""

        return f"""
You are a professional children's story writer.

Write an ORIGINAL children's story.

Never copy existing stories.

----------------------------------------
Research

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

Research:
{research_report.research}

----------------------------------------
Official Character Bible

{characters}

----------------------------------------
Rules

Use ONLY the characters provided.

Never change their appearance.

Never change their clothing.

Never change their accessories.

Never change their personality.

Keep every character visually consistent.

Never invent new main characters.

Only introduce tiny side characters if absolutely necessary.

Story Structure

Beginning

Problem

Adventure

Climax

Ending

Moral

Language Rules

Simple English

Age 5–8

Fun

Funny

Educational

Family Friendly

No violence

No horror

No politics

No religion

No copyrighted characters

Story Length

Approximately 350–450 words.

----------------------------------------

Return ONLY valid JSON.

JSON Schema

{{
    "title": "",
    "story": "",
    "moral": "",
    "word_count": 0
}}
"""