class WorkflowRegistry:

    def __init__(self):

        self._workflows = {}

    def register(
        self,
        name,
        workflow
    ):

        self._workflows[name] = workflow

    def get(
        self,
        name
    ):

        return self._workflows.get(name)

    def list(self):

        return list(self._workflows.keys())