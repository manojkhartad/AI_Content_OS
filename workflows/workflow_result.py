from dataclasses import dataclass
from typing import Any


@dataclass
class WorkflowResult:

    story: Any = None
    scenes: Any = None
    narrations: Any = None
    images: Any = None
    audio: Any = None
    video: Any = None