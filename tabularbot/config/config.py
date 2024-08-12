from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os

load_dotenv()


class Workspace(BaseModel):
    dir_path: str
    open_ai_key: str = Field(default_factory=lambda: os.getenv("OPEN_AI_KEY"))
