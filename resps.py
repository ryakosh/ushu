from pydantic import BaseModel

class ShortenedUrlRes(BaseModel):
    shortened: str
