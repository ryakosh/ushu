from pydantic import BaseModel

class ShortenedUrlRes(BaseModel):
    shortened: str

class ExpandedUrlRes(BaseModel):
    expanded: str
