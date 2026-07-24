import logging
from pathlib import Path


Path("logs").mkdir(exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/aira.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("AIRA")