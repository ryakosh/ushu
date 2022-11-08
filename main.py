from fastapi import FastAPI, HTTPException
from hashids import Hashids
from peewee import OperationalError

import configs
from models import db, Url
from resps import ShortenedUrlRes, ExpandedUrlRes
from reqs import ShortenUrlReq, ExpandUrlReq

app = FastAPI()
with db:
    db.create_tables([Url])

hids = Hashids(
    salt=configs.USHU_HASHIDS_SALT,
    min_length=configs.USHU_HASHIDS_MINLEN)

@app.on_event("startup")
def startup():
    db.connect()

@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()

@app.post('/shorten')
async def shorten(req: ShortenUrlReq): 
    model = Url.create(url=req.url) 
    res = ShortenedUrlRes(shortened=hids.encode(model.id))
    return res

@app.get('/expand')
async def expand(req: ExpandUrlReq):
    uid = hids.decode(req.short_url)
    if uid:
        url = Url.get(hids.decode(req.short_url))
        if url:
            return ExpandedUrlRes(expanded=url.url)
    return HTTPException(status_code=404) 
