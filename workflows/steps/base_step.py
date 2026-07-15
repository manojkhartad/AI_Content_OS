from abc import ABC, abstractmethod

from workflows.workflow_context import WorkflowContext


class BaseStep:

    @abstractmethod
    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:
        pass