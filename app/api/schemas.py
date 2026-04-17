from pydantic import BaseModel
from typing import Literal

class ChatRequest(BaseModel):
    data: str