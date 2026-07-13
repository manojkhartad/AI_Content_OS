# ==========================================================
# Image Prompt Generator
# ==========================================================

class ImagePromptPrompt:

    @staticmethod
    def generate(scene, character_bibles):

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
--------------------------------------------------
"""

        return f"""
You are an expert AI Image Prompt Engineer.

Your task is to create ONE professional image generation prompt for a children's animated story.

The prompt will later be used with AI image models.

==================================================

SCENE INFORMATION

Scene Number:
{scene.scene_number}

Scene Title:
{scene.title}

Scene Summary:
{scene.summary}

Location:
{scene.location}

Time of Day:
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

==================================================

CHARACTERS

{character_info}

==================================================

INSTRUCTIONS

Generate ONE cinematic image prompt.

The image should:

- Keep every character visually consistent.
- Follow the Character Bible exactly.
- Match the scene emotion.
- Match the scene location.
- Match the time of day.
- Include cinematic composition.
- Include professional lighting.
- Include depth of field.
- Include high detail.
- Include colorful children's animation style.
- Keep the same character design across every scene.

Style:

Pixar-quality 3D animated movie.

==================================================

Return ONLY valid JSON.

Expected Format

{{
    "scene_id":"{scene.scene_id}",
    "scene_number":{scene.scene_number},
    "title":"{scene.title}",
    "positive_prompt":"...",
    "negative_prompt":"blurry, low quality, watermark, logo, text, cropped, deformed, duplicate, bad anatomy, extra limbs",
    "style":"Pixar 3D Animated Movie",
    "aspect_ratio":"16:9",
    "image_size":"1024x576"
}}

Return ONLY JSON.
"""