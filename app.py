from core.logger import logger
from core.config import config
from core.plugin_manager import plugin_manager


def main():

    logger.info(
        "AIRA Starting..."
    )


    logger.info(
        f"Version {config.get('version')}"
    )


    plugin_manager.load_plugins()


    logger.info(
        "Plugin Manager Ready"
    )


    logger.info(
        "AIRA System Online"
    )



if __name__ == "__main__":
    main()