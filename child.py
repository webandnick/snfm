from sqlalchemy import Table,Column,Integer,String,ForeignKey,create_engine,MetaData
from sqlalchemy.orm import relationship,sessionmaker,mapper
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/fam.db',echo=True)
Session = sessionmaker(bind=engine)
metadata = MetaData()
from parent import Parent,parent



child = Table("child",metadata,
              Column("id",Integer, primary_key=True),
              Column("parent_id",Integer, ForeignKey('parent.id')),





              )

class Child():
    def __init__(self,parent):
        self.parent = parent

mapper(Parent,parent,properties={"child":relationship(Child,backref="parent")})
mapper(Child,child)