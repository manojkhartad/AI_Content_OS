print("===================================")
print("      AI Content OS Started")
print("===================================")

from agents.agent_manager import AgentManager
from memory.memory_manager import MemoryManager

from workflows.workflow_context import WorkflowContext
from workflows.workflow_manager import WorkflowManager
from workflows.story_workflow import StoryWorkflow


manager = AgentManager()

memory = MemoryManager()

context = WorkflowContext(
    topic="Lion and Rabbit"
)

workflow = StoryWorkflow()

workflow_manager = WorkflowManager()

result = workflow_manager.run(
    workflow,
    context
)