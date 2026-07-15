from workflows.base_workflow import BaseWorkflow
from workflows.workflow_context import WorkflowContext
from workflows.workflow_result import WorkflowResult


class WorkflowManager:

    def run(
        self,
        workflow: BaseWorkflow,
        context: WorkflowContext
    ) -> WorkflowResult:

        return workflow.run(context)