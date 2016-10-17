from sqlalchemy import  Column,Integer,String,ForeignKey,Table
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tests.db'
db = SQLAlchemy(app)




class User(db.Model):
    id = Column(Integer,primary_key=True)
    name = Column(String(50),unique=True)
    email = Column(String(50),unique=True)
    password = Column(String(50))


    def __init__(self,name=None,email=None,password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return  "<User: (%s) >" % (str(self.id))



if __name__ == "__main__":
    db.create_all()
    u = User(name="fe",email="yo",password="nope")
    db.session.add(u)
    db.session.commit()