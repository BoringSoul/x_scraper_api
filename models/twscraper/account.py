from pydantic import BaseModel

class TweetAccountInfo(BaseModel):
    username: str
    cookies: str