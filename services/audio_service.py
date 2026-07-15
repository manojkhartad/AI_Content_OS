from services.base_service import BaseService


class AudioService(BaseService):

    def __init__(self):
        super().__init__("Audio Service")

    def execute(self, *args, **kwargs):
        self.start()