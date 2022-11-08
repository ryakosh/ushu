import os

from fastapi import FastAPI
from dotenv import load_dotenv
from hashids import Hashids

from models import db, Url
from resps import ShortenedUrlRes
from reqs import ShortenUrlReq

load_dotenv()
app = FastAPI()
with db:
    db.create_tables([Url])

try:
    hids = Hashids(salt=os.environ['USHU_HASHIDS_SALT'])
except KeyError:
    print("ERR: 'USHU_HASHIDS_SALT' Not Set")

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
