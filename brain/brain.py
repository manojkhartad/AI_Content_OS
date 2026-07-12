from brain.llm_client import LLMClient


class Brain:

    def think(self, topic):

        print("Brain Thinking...")

        llm = LLMClient()

        prompt = f"""
Research this topic for a kids educational story:

Topic: {topic}

Reply in 5-6 simple sentences.
"""

        response = llm.generate(prompt)

        print(response)

        return {
            "goal": "Educational + Fun",
            "tone": "Funny",
            "target_audience": "5-8 Years"
        }