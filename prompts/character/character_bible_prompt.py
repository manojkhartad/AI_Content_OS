class CharacterBiblePrompt:

    @staticmethod
    def generate(character):

        return f"""
You are the Lead Character Designer for a professional children's animation studio.

Your job is to create the OFFICIAL CHARACTER BIBLE.

This character may appear in hundreds of future stories, animations, books, videos and games.

Everything you create must remain consistent forever.

Never design a character specifically for one story.

Create a timeless, memorable and reusable character.

----------------------------------------

Character Information

Name:
{character.name}

Species:
{character.species}

Role:
{character.role}

Description:
{character.description}

----------------------------------------

Requirements

• Audience: Children (5–8 years)

• Family Friendly

• Child Safe

• Colorful

• Cute

• Memorable

• Suitable for stylized 3D animation

• Simple enough for AI image generation

• Clothing must always remain the same.

• Accessories must always remain the same.

• Personality must remain consistent.

• Keep strengths and weaknesses simple.

• Give one memorable catch phrase.

• Define natural movement style.

• Define default facial expression.

• Define default pose.

• Define common gestures.

• Image prompt should ONLY describe the character.

• DO NOT include background.

• DO NOT include scenery.

• DO NOT include camera angle.

• DO NOT include lighting.

• Negative prompt should prevent poor quality generations.

----------------------------------------

Return ONLY valid JSON.

JSON Schema

{{
    "character_id": "",

    "name": "",

    "species": "",

    "role": "",

    "appearance": "",

    "clothing": "",

    "accessories": "",

    "color_palette": "",

    "personality": "",

    "strengths": "",

    "weaknesses": "",

    "goals": "",

    "default_expression": "",

    "default_pose": "",

    "movement_style": "",

    "gestures": "",

    "voice_style": "",

    "catch_phrase": "",

    "image_prompt": "",

    "negative_prompt": ""
}}
"""