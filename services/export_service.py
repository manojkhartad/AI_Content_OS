from services.base_service import BaseService


class ExportService(BaseService):

    def __init__(self):
        super().__init__("Export Service")

    def execute(self, *args, **kwargs):
        self.start()