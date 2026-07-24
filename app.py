from core.logger import logger
from core.config import config
from core.plugin_manager import plugin_manager

from ai.chat import chat_ai


def main():

    logger.info("AIRA Starting...")

    logger.info(
        f"Version {config.get('version')}"
    )

    # プラグイン読み込み
    plugin_manager.load_plugins()

    logger.info(
        "Plugin Manager Ready"
    )

    logger.info(
        "AI Engine Ready"
    )


    while True:

        try:

            text = input("\nあなた > ")

            if text.lower() in [
                "exit",
                "quit",
                "終了"
            ]:
                logger.info(
                    "AIRA Shutdown"
                )
                break


            answer = chat_ai.ask(text)


            print(
                "AIRA >",
                answer
            )


        except KeyboardInterrupt:

            print("\n終了します")
            break


        except Exception as e:

            logger.error(e)



if __name__ == "__main__":
    main()