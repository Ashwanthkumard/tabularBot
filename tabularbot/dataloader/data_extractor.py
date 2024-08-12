import csv
import io
import logging
import os

from pydantic import BaseModel
from pymupdf import pymupdf, FileDataError
from openai import OpenAI
import pandas as pd

from tabularbot.config.config import Workspace
from tabularbot.prompts.unstructured_data_cleaning_prompt import UnstructuredDataCleaning

logger = logging.getLogger(__name__)


class InvoiceDataExtraction(BaseModel):
    data: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True


class ExtractData:
    def __init__(self, workspace: Workspace):
        self.dir_path = workspace.dir_path
        self.opena_ai_key = workspace.open_ai_key

    @staticmethod
    def get_all_files(dic_path) -> list:
        return os.listdir(dic_path)

    @staticmethod
    def extract_data_from_file(file) -> str:
        try:
            doc = pymupdf.open(file)
            all_text = ""
            for page in doc:
                text = page.get_text()
                all_text += text
            return all_text
        except FileDataError:
            logger.error("Failed loading file : ", file)
            return ""

    def extract_tabular_data(self) -> pd.DataFrame:
        files = self.get_all_files(self.dir_path)
        logger.info(f"Directory has {len(files)} files")

        all_data = []

        client = OpenAI(
            api_key=self.opena_ai_key,
        )

        for file in files:
            completion = client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system",
                     "content": UnstructuredDataCleaning.prompt},
                    {"role": "user", "content": self.extract_data_from_file(os.path.join(self.dir_path, file))}
                ],
                # response_format=InvoiceDataExtraction,
            )
            csv_content = completion.choices[0].message.content.strip("```csv\n").strip("```")

            # Parse the CSV content
            csv_reader = csv.DictReader(io.StringIO(csv_content))
            data = pd.DataFrame(csv_reader, columns=['BrandName', 'Qty', 'Price'])
            all_data.append(data)

            return pd.concat(all_data, ignore_index=True, axis=0)
