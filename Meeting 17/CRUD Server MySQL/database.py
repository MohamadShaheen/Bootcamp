from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_database = 'mysql+pymysql://root:test1234!@localhost:3306/classicmodels'

engine = create_engine(URL_database)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
