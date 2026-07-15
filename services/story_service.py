from services.base_service import BaseService


class StoryService(BaseService):

    def __init__(self):
        super().__init__("Story Service")

    def execute(self, *args, **kwargs):
        self.start()