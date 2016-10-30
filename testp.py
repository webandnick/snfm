from testm import pwe , User, db

class Post(pwe.Model):
    user = pwe.ForeignKeyField(User,related_name="posts")
    head = pwe.CharField()
    class Meta:
        database = db

