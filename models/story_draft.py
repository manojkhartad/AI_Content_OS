from dataclasses import dataclass


@dataclass
class StoryDraft:
    title: str
    story: str
    moral: str
    word_count: int