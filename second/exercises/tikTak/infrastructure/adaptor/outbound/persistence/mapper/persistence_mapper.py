from second.exercises.tikTak.domain.result import Result
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.entity.result_entity import ResultEntity


class PersistenceMapper:
    @staticmethod
    def map_to_result_entity(result: Result) -> ResultEntity:
        return ResultEntity(
            name=result.winner_name,
            is_game_board_free_space_available=result.is_game_board_free_space_available
        )

    @staticmethod
    def map_to_result(results: [ResultEntity]) -> list[Result]:
        return list(map(lambda entity: Result(entity.name, entity.is_game_board_free_space_available), results))
