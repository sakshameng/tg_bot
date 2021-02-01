from sqlalchmey import create_engine
from sqlalchmey.ext.declarative import declarative_base
from sqlalchmey.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


def start() -> scoped_session:
  engine = create.engine(DB_URI, client_encoding="utf8")
  BASE.metadata.bind = engine
  BASE.metadata.create_all(engine)
  return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()