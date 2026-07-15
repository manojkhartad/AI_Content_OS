from dataclasses import dataclass, field
from typing import Any, Dict

from utils.performance_profiler import PerformanceProfiler


@dataclass
class WorkflowContext:

    topic: str

    data: Dict[str, Any] = field(default_factory=dict)

    profiler: PerformanceProfiler = field(
        default_factory=PerformanceProfiler
    )

    def set(self, key, value):

        self.data[key] = value

    def get(self, key, default=None):

        return self.data.get(key, default)