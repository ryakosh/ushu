from pydantic import BaseModel, HttpUrl, Field

import cfg

class ShortenUrlReq(BaseModel):
    """Represents a request to shorten a fully qualified URL."""

    url: HttpUrl

class ExpandUrlReq(BaseModel):
    """
    Represents a request to expand or resolve a
    previously shortened URL.
    """

    short_url: str = Field(
        min_length=cfg.USHU_HASHIDS_MINLEN,
        max_length=cfg.USHU_SHORTURL_MAXLEN)
