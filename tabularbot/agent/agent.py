import logging

from openai import OpenAI

from tabularbot.config.config import Workspace
from tabularbot.dataloader.data_extractor import ExtractData

logger = logging.getLogger(__name__)


class TabularDataAgent:
    def __init__(self, data_folder):
        self.ws = Workspace(dir_path=data_folder)

    def run(self):
        data_extractor = ExtractData(self.ws)
        data = data_extractor.extract_tabular_data()

        client = OpenAI(
            api_key=self.ws.open_ai_key,
        )

        while True:
            # Take input from the user
            user_input = input("User Question (or exit/quit to stop)-> ")

            # Check if the user wants to quit
            if user_input.lower() in ["exit", "quit"]:
                logger.warning("Terminating the process!")
                break

            try:
                completion = client.chat.completions.create(
                    model="gpt-4o-2024-08-06",
                    messages=[
                        {"role": "system",
                         "content": "You are a helpful assistant. Please help me answer the following question from "
                                    "the csv data. ".format(user_input)},  # <-- This is the system message that
                        # provides context to the model
                        {"role": "user", "content": data.to_string()}
                    ]
                )

                print("Assistant: " + completion.choices[0].message.content)
            except Exception as e:
                logger.error(f"Error: {e}")
