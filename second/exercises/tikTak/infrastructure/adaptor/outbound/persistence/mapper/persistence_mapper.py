from second.exercises.tikTak.domain.result import Result
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.entity.result_entity import ResultEntity


class PersistenceMapper:
    @staticmethod
    def map_to_result_entity(result: Result) -> ResultEntity:
        return ResultEntity(name=result.winner_name, is_game_board_full=result.is_game_board_full)

    @staticmethod
    def map_to_result(results: [ResultEntity]) -> [Result]:
        return [map(lambda entity: Result(entity.name, entity.is_game_board_full), results)]
