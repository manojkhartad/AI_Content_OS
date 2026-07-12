print("===================================")
print("      AI Content OS Started")
print("===================================")

from agents.agent_manager import AgentManager
from memory.memory_manager import MemoryManager
from workflows.story_workflow import StoryWorkflow


manager = AgentManager()

memory = MemoryManager()

workflow = StoryWorkflow()

workflow.run("Lion and Rabbit")