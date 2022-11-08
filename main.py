from fastapi import FastAPI, HTTPException
from hashids import Hashids

import cfg
from models import db, UrlModel
from resps import ShortenedUrlRes, ExpandedUrlRes
from reqs import ShortenUrlReq, ExpandUrlReq

app = FastAPI()
with db:
    db.create_tables([UrlModel])

hids = Hashids(
    salt=cfg.USHU_HASHIDS_SALT,
    min_length=cfg.USHU_HASHIDS_MINLEN)

@app.on_event("startup")
def startup():
    db.connect()

@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()

@app.post('/shorten')
async def shorten(req: ShortenUrlReq): 
    """Shortens a fully qualified URL to an alphanumeric string."""

    urlmod = UrlModel.create(url=req.url) 
    res = ShortenedUrlRes(shortened=hids.encode(urlmod.id))
    return res

@app.get('/expand')
async def expand(req: ExpandUrlReq):
    """Expands or resolves a shortened url to it's original form."""

    urlmod_id = hids.decode(req.short_url)
    if urlmod_id:
        urlmod = UrlModel.get(urlmod_id)
        if urlmod:
            return ExpandedUrlRes(expanded=urlmod.url)
    return HTTPException(status_code=404) 
