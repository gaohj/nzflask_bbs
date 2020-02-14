from sqlalchemy import Column,Integer,String
from utils.db import Base

def create_db():
    Base.metadata.create_all()

def drop_db():
    Base.metadata.drop_all()


class Students(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    s_name = Column(String(30),nullable=False,unique=True)
    s_age = Column(Integer,default=18)

    __tablename__ = 'students'

    def __repr__(self):
        return "Students(name:%s,age:%s)" % (self.s_name,self.s_age)