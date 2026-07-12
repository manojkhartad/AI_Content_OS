class BasePrompt:

    def __init__(
        self,
        content_type,
        target_audience,
        goal,
        tone
    ):

        self.content_type = content_type
        self.target_audience = target_audience
        self.goal = goal
        self.tone = tone

    def build(self, topic):
        """
        Every Prompt must implement this.
        """
        raise NotImplementedError(
            "Child Prompt must implement build()"
        )