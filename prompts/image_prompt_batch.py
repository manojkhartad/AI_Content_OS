# ==========================================================
# Batch Image Prompt Generator
# ==========================================================

class ImagePromptBatchPrompt:

    @staticmethod
    def generate(scenes, character_bibles):

        scenes_text = ""

        for scene in scenes:

            character_info = ""

            for character in character_bibles:

                if character.character_id in scene.characters:

                    character_info += f"""
Character ID: {character.character_id}
Name: {character.name}
Species: {character.species}
Role: {character.role}

Appearance:
{character.appearance}

Clothing:
{character.clothing}

Accessories:
{character.accessories}

Color Palette:
{character.color_palette}

Default Expression:
{character.default_expression}

Default Pose:
{character.default_pose}

Movement Style:
{character.movement_style}

Gestures:
{character.gestures}

----------------------------------------
"""

            scenes_text += f"""
==================================================
SCENE {scene.scene_number}

Scene ID:
{scene.scene_id}

Title:
{scene.title}

Summary:
{scene.summary}

Location:
{scene.location}

Time Of Day:
{scene.time_of_day}

Emotion:
{scene.emotion}

Narration:
{scene.narration}

Dialogue:
{scene.dialogue}

Visual Notes:
{scene.visual_notes}

Continuity Notes:
{scene.continuity_notes}

CHARACTERS

{character_info}

==================================================
"""

        return f"""
You are an expert AI Image Prompt Engineer.

Generate professional Pixar-quality image prompts for ALL scenes.

Generate ONE image prompt per scene.

Follow every Character Bible exactly.

Maintain perfect character consistency across every scene.

==================================================

SCENES

{scenes_text}

==================================================

OUTPUT RULES

Return ONLY valid JSON.

Return a JSON array.

Each object must match this format exactly.

[
    {{
        "scene_id":"",
        "scene_number":1,
        "title":"",
        "positive_prompt":"",
        "negative_prompt":"blurry, low quality, watermark, logo, text, cropped, deformed, duplicate, bad anatomy, extra limbs",
        "style":"Pixar 3D Animated Movie",
        "aspect_ratio":"16:9",
        "image_size":"1024x576"
    }}
]

Return ONLY the JSON array.
"""