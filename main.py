print("===================================")
print("      AI Content OS Started")
print("===================================")

from agents.agent_manager import AgentManager
from memory.memory_manager import MemoryManager
from workflows.story_workflow import StoryWorkflow

manager = AgentManager()
memory = MemoryManager()
workflow = StoryWorkflow()

story = workflow.run("Lion and Rabbit")

print("\n==============================")
print("Story Generated Successfully")
print("==============================\n")

print("Title:")
print(story.title)

print("\nStory:")
print(story.story)

print("\nMoral:")
print(story.moral)

print("\nWord Count:")
print(story.word_count)