from pydantic import BaseModel, HttpUrl, Field

import configs

class ShortenUrlReq(BaseModel):
    url: HttpUrl

class ExpandUrlReq(BaseModel):
    short_url: str = Field(
        min_length=configs.USHU_HASHIDS_MINLEN,
        max_length=configs.USHU_SHORTURL_MAXLEN)
