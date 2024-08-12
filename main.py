import logging

from logging_config import setup_logging
from tabularbot.agent.agent import TabularDataAgent
import sys

setup_logging()
logger = logging.getLogger(__name__)


def main(data_dir):
    agent = TabularDataAgent(data_dir)
    agent.run()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.warning("Usage: python main.py <data_folder>")
        sys.exit(1)

    data_dir = sys.argv[1]
    main(data_dir)
