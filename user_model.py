from sqlalchemy import  Column,Integer,String,ForeignKey,Table,MetaData,create_engine
from sqlalchemy.orm import backref,relationship,mapper,sessionmaker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tests.db'
db = SQLAlchemy(app)


metadata = MetaData()
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)


user = Table("user",metadata,
             Column("id",Integer,primary_key=True),
             Column("name",String(63),unique=True),
             Column("pwd",String(63))
             


             )

class User(object):
    def __init__(self,name):
        self.name = name




if __name__ == "__main__":
    db.create_all()
    u = User(name="fe",email="yo",password="nope")
    db.session.add(u)
    db.session.commit()