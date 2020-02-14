from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#连接数据库
db_uri = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado_nz'

#创建数据库引擎 建立连接
engine = create_engine(db_uri)

#创建基类  方便后边创建模型
Base = declarative_base(bind=engine)

#数据库的增删改查 需要  session对象
session = sessionmaker(bind=engine)()
