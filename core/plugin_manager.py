from pathlib import Path
import importlib


class PluginManager:


    def __init__(self):

        self.plugins = []



    def load_plugins(self):

        folder = Path("plugins")

        if not folder.exists():
            return


        for file in folder.glob("*.py"):

            if file.name == "__init__.py":
                continue

            module = importlib.import_module(
                f"plugins.{file.stem}"
            )

            self.plugins.append(module)



    def list_plugins(self):

        return self.plugins



plugin_manager = PluginManager()