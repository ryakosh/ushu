from pydantic import BaseModel

class ShortenedUrlRes(BaseModel):
    """Represents a response to shortening a URL."""

    shortened: str

class ExpandedUrlRes(BaseModel):
    """Represents a response to expanding or resolving a URL."""

    expanded: str
