import os
from peewee import Model, CharField, DateTimeField, ForeignKeyField, TextField
from playhouse.db_url import connect

db = connect(os.environ.get("DATABASE_URL", "sqlite:///saravjishut.db"))


class User(Model):
    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

    class Meta:
        database = db


class Post(Model):
    name = ForeignKeyField(model=User, null=True)
    date = DateTimeField(null=True)
    subject = CharField(max_length=255)
    content = TextField()

    class Meta:
        database = db
