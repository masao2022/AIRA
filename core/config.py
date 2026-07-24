import json
from pathlib import Path


class Config:

    def __init__(self):
        self.path = Path("config/config.json")
        self.data = {}

        self.load()


    def load(self):

        if self.path.exists():

            with open(
                self.path,
                "r",
                encoding="utf-8"
            ) as f:
                self.data = json.load(f)

        else:
            print("config.json not found")


    def get(self, key, default=None):

        return self.data.get(key, default)


config = Config()