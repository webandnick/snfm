from sqlalchemy import  Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import relationship,backref,mapper
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user_model import User,user,metadata,engine,Session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tests.db'
db = SQLAlchemy(app)



post = Table("post",metadata,
             Column("id",Integer,primary_key=True),
             Column("head",String(64)),
             Column("user_id",Integer,ForeignKey("user.id")))



class Post(object):
    def __init__(self,head):
        self.head = head


    def __repr__(self):
        return  "<Post: (%s) >" % (str(self.id))


mapper(Post,post)
mapper(User,user,properties={"posts":relationship(Post,backref="user")})

if __name__ == "__main__":
    pass


