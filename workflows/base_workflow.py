from abc import ABC, abstractmethod

from workflows.workflow_context import WorkflowContext
from workflows.workflow_result import WorkflowResult


class BaseWorkflow(ABC):

    @abstractmethod
    def run(
        self,
        context: WorkflowContext
    ) -> WorkflowResult:
        pass