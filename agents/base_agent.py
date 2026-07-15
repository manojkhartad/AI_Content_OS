from abc import ABC, abstractmethod


class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name

    def start(self):
        print(f"{self.name} Started")

    @abstractmethod
    def run(self, *args, **kwargs):
        pass