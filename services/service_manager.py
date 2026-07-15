from services.base_service import BaseService
from services.service_factory import ServiceFactory


class ServiceManager(BaseService):

    _instances = {}

    def __init__(self):
        super().__init__("Service Manager")

    def get(self, name: str):

        if name not in self._instances:

            self._instances[name] = (
                ServiceFactory.create(name)
            )

        return self._instances[name]

    def execute(self, *args, **kwargs):
        self.start()