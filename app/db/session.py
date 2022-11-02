import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

database = databases.Database(settings.DB_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(settings.DB_URL)
metadata.create_all(engine)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
