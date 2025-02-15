from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.entity.base import Base


class Engine:
    _engine = create_engine("postgresql://username:password@127.0.0.1:5432/db")
    _session = sessionmaker(bind=_engine)

    def __init__(self):
        Base.metadata.create_all(Engine._engine)
        Engine._engine.connect()

    def create_session(self):
        return self._session()
