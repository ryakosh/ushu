from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase('ushu.db', autoconnect=False)

class BaseModel(Model):
    class Meta:
        database = db

class Url(BaseModel):
    url = CharField(null=False, max_length=2083)

