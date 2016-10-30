import peewee as pwe

db = pwe.SqliteDatabase("/tmp/d.db")

class User(pwe.Model):

    name = pwe.CharField()
    class Meta:
        database = db


