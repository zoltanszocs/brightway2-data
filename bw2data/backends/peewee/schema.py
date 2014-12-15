from peewee import Model, TextField, BlobField
from . import sqlite3_db


class ActivityDataset(Model):
    data = BlobField()
    key = TextField(index=True, unique=True)
    database = TextField()
    location = TextField(null=True)
    name = TextField(null=True)
    product = TextField(null=True)

    class Meta(object):
        database = sqlite3_db


class ExchangeDataset(Model):
    data = BlobField()
    input_ = TextField(index=True)
    output = TextField(index=True)
    database = TextField(index=True)
    type_ = TextField()

    class Meta(object):
        database = sqlite3_db
