from sqlalchemy import Table,Column,Integer,String,ForeignKey,create_engine,MetaData
from sqlalchemy.orm import relationship,sessionmaker,mapper
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/fam.db',echo=True)
Session = sessionmaker(bind=engine)

metadata = MetaData()


parent = Table("parent",metadata,
              Column("id",Integer,primary_key=True),
              )


class Parent():
    def __init__(self,child):
        self.child = child


