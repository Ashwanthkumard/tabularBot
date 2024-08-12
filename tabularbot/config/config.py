from pydantic import BaseModel
import os

from tabularbot.prompts.base import BasePrompt


class Workspace(BaseModel):
    dir_path: str
    open_ai_key: os.getenv("OPEN_AI_KEY")
    # prompt: BasePrompt
