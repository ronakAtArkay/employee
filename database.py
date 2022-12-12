from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "mysql+mysqlconnector://root:%s@localhost:3306/employee" % quote("Arkay@210")

engin = create_engine(url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()
