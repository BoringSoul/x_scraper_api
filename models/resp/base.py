from typing import Any
from pydantic import BaseModel

class Resp(BaseModel):
    code: int
    message: str
    data: Any