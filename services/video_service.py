from services.base_service import BaseService


class VideoService(BaseService):

    def __init__(self):
        super().__init__("Video Service")

    def execute(self, *args, **kwargs):
        self.start()