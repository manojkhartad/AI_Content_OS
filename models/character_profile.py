from dataclasses import dataclass


@dataclass
class CharacterProfile:
    name: str
    role: str
    species: str
    description: str