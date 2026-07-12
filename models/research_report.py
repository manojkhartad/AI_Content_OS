from dataclasses import dataclass


@dataclass
class ResearchReport:
    topic: str
    content_type: str
    target_audience: str
    goal: str
    tone: str