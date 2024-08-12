from tabularbot.agent.agent import TabularDataAgent
import sys


def main(data_folder):
    agent = TabularDataAgent(data_folder)
    agent.run()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <data_folder>")
        sys.exit(1)

    data_folder = sys.argv[1]
    main(data_folder)
