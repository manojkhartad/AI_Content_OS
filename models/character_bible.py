from dataclasses import dataclass


@dataclass
class CharacterBible:

    # Identity

    character_id: str

    name: str

    species: str

    role: str

    # Visual Design

    appearance: str

    clothing: str

    accessories: str

    color_palette: str

    # Personality

    personality: str

    strengths: str

    weaknesses: str

    goals: str

    # Animation

    default_expression: str

    default_pose: str

    movement_style: str

    gestures: str

    # Voice

    voice_style: str

    catch_phrase: str

    # Production

    image_prompt: str

    negative_prompt: str