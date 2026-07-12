class BaseAgent:

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} Started")