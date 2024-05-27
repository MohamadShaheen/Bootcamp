from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_URL = 'mysql+pymysql://root:@localhost:3306/pokemonsdatabase'

engine = create_engine(database_URL)

session_local = sessionmaker(bind=engine)

Base = declarative_base()
