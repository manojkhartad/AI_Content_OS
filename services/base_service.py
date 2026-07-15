from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self, name: str):
        self.name = name

    def start(self):
        print(f"{self.name} Started")

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass