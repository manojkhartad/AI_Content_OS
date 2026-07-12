from dataclasses import dataclass


@dataclass
class ReviewReport:

    passed: bool

    score: int

    feedback: str