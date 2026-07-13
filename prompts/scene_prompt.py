# ==========================================================
# Scene Generation Prompt
# ==========================================================

SCENE_PROMPT = """
You are an expert Children's Story Scene Planner.

Your job is NOT to rewrite the story.

Your job is to break the story into a sequence of visual scenes.

The scenes will later be used for:

- Story Illustration
- AI Image Generation
- AI Animation
- AI Video Generation

------------------------------------------------------------

RULES

1. Read the entire story carefully.

2. Divide the story into 6 to 10 logical scenes.

3. Every scene should represent one important event.

4. Keep continuity between scenes.

5. Never skip important story events.

6. Use simple language.

7. Keep narration concise.

8. Dialogue should only contain spoken words.

9. Visual notes should describe what should be visible on screen.

10. Do NOT invent new characters.

11. Do NOT change the story.

------------------------------------------------------------

For EACH scene provide:

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

------------------------------------------------------------

Return ONLY valid JSON.

Expected JSON format:

{
    "title": "Story Title",
    "total_scenes": 6,
    "scenes":
    [
        {
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
        }
    ]
}

------------------------------------------------------------

Story:

{story}
"""