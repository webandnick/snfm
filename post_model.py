from sqlalchemy import  Column,Integer,String,ForeignKey,Table
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tests.db'
db = SQLAlchemy(app)




class Post(db.Model):
    id = Column(Integer,primary_key=True)
    head = Column(String(127))
    body = Column(String(511))
    user_id = Column(Integer,ForeignKey("user.id"))
    user = db.relationship("User",backref=db.backref("post",lazy="dynamic"))

    def __init__(self,head=None,body=None,user=None):
        self.head = head
        self.body = body
        self.user = user


    def __repr__(self):
        return  "<Post: (%s) >" % (str(self.id))


if __name__ == "__main__":
    from user_model import  User
    db.create_all()
    p = Post(head="hello",body="world",user=User.query.first())
    db.session.add(p)
    db.session.commit()



