from agents.research_agent import ResearchAgent
from agents.character_agent import CharacterAgent
from agents.character_bible_agent import CharacterBibleAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent
from agents.scene_agent import SceneAgent
from agents.narration_agent import NarrationAgent
from agents.image_prompt_agent import ImagePromptAgent
from agents.image_generation_agent import ImageGenerationAgent
from agents.tts_agent import TTSAgent
from agents.video_generation_agent import VideoGenerationAgent


AGENT_REGISTRY = {
    "research": ResearchAgent,
    "character": CharacterAgent,
    "character_bible": CharacterBibleAgent,
    "writer": WriterAgent,
    "reviewer": ReviewerAgent,
    "scene": SceneAgent,
    "narration": NarrationAgent,
    "image_prompt": ImagePromptAgent,
    "image_generation": ImageGenerationAgent,
    "tts": TTSAgent,
    "video_generation": VideoGenerationAgent,
}