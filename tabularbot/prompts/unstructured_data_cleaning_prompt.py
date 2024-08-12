from tabularbot.prompts.base import BasePrompt


class UnstructuredDataCleaning(BasePrompt):
    prompt = ("You are an expert in structured data extraction. You will be provided with unstructured text from "
              "invoices, and your task is to extract and return the BrandName, Quantity, and Price in CSV format.")