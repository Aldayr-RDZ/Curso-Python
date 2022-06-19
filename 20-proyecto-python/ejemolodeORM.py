from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
engine= create_engine('Server=Prueba;Database=Servicio;Port=localhost:5432;UID=postgres;Password=1801769')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()