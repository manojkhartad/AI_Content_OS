from pathlib import Path
import json


class CheckpointManager:
    def __init__(self, checkpoint_file="production/checkpoint.json"):
        self.checkpoint_file = Path(checkpoint_file)

    def load(self):
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save(self, data):
        self.checkpoint_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.checkpoint_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def clear(self):
        if self.checkpoint_file.exists():
            self.checkpoint_file.unlink()