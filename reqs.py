from pydantic import BaseModel, HttpUrl

class ShortenUrlReq(BaseModel):
    url: HttpUrl
