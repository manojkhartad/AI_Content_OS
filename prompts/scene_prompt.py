# ==========================================================
# Scene Prompt
# ==========================================================

class ScenePrompt:

    @staticmethod
    def generate(story, character_bibles):

        characters = ""

        for character in character_bibles:

            characters += f"""
Character ID: {character.character_id}
Name: {character.name}
Species: {character.species}
Role: {character.role}

Appearance: {character.appearance}
Clothing: {character.clothing}
Accessories: {character.accessories}
Color Palette: {character.color_palette}

Personality: {character.personality}
Strengths: {character.strengths}
Weaknesses: {character.weaknesses}
Goals: {character.goals}

Default Expression: {character.default_expression}
Default Pose: {character.default_pose}
Movement Style: {character.movement_style}
Gestures: {character.gestures}

Voice Style: {character.voice_style}
Catch Phrase: {character.catch_phrase}

--------------------------------------------------
"""

        return f"""
You are an expert Storyboard Artist and Children's Story Scene Planner.

Your task is to convert the children's story into a sequence of visual scenes.

The scenes will later be used for:

- AI Image Generation
- AI Animation
- AI Video Generation

==================================================

STORY TITLE

{story.title}

==================================================

MORAL

{story.moral}

==================================================

CHARACTER BIBLES

{characters}

==================================================

STORY

{story.story}

==================================================

INSTRUCTIONS

1. Divide the story into 6–10 logical scenes.

2. Each scene should represent ONE important event.

3. Maintain chronological order.

4. Never skip important events.

5. Never invent new characters.

6. Always use the Character Bible for appearance and personality consistency.

7. Narration should describe what happens.

8. Dialogue should contain ONLY spoken words.

9. Visual Notes should describe exactly what should be visible on screen.

10. Continuity Notes should help the next scene remain visually consistent.

11. Keep every scene child-friendly.

12. Keep every scene visually interesting.

==================================================

For EACH scene generate:

scene_id
scene_number
title
summary
purpose
location
time_of_day
characters
narration
dialogue
emotion
visual_notes
continuity_notes

==================================================

Return ONLY valid JSON.

Expected Format

{{
    "title": "Story Title",
    "total_scenes": 8,
    "scenes": [
        {{
            "scene_id": "SCENE_001",
            "scene_number": 1,
            "title": "",
            "summary": "",
            "purpose": "",
            "location": "",
            "time_of_day": "",
            "characters": [],
            "narration": "",
            "dialogue": "",
            "emotion": "",
            "visual_notes": "",
            "continuity_notes": ""
        }}
    ]
}}

Return ONLY JSON.
"""