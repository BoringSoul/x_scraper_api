from pydantic import BaseModel

class SearchReq(BaseModel):
    q: str
    kv: dict = {"product": "top"}
    limit: int = 100