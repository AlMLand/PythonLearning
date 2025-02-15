from second.exercises.tikTak.application.port.outbound.persistence_port import PersistencePort
from second.exercises.tikTak.domain.result import Result
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.database_engine.engine import Engine
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.entity.result_entity import ResultEntity
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.mapper.persistence_mapper import \
    PersistenceMapper


class PersistenceAdaptor(PersistencePort):
    def __init__(self):
        self.db_engine = Engine()
        self.mapper = PersistenceMapper()

    def create_result(self, result: Result):
        entity = self.mapper.map_to_result_entity(result)
        with self.db_engine.create_session() as session:
            session.add(entity)
            session.commit()

    def get_all_results(self) -> list[Result]:
        with self.db_engine.create_session() as session:
            entities = session.query(ResultEntity).all()
            return self.mapper.map_to_result(entities)
