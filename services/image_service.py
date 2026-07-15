from services.base_service import BaseService


class ImageService(BaseService):

    def __init__(self):
        super().__init__("Image Service")

    def execute(self, *args, **kwargs):
        self.start()