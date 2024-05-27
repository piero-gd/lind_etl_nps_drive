from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.env_config import DB_CONNECTION_STRING

class DatabaseConfig:
    def __init__(self):
        self.connection_string = DB_CONNECTION_STRING
        self.engine = create_engine(self.connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def get_engine(self):
        return self.engine

    def create_session(self):
        return self.Session()
    