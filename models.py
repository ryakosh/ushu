from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase('ushu.db', autoconnect=False)

class BaseModel(Model):
    """The base model!, Every other model should inherit from this."""

    class Meta:
        database = db

class UrlModel(BaseModel):
    """Represents a URL model/table in the database."""

    url = CharField(null=False, max_length=2083)

