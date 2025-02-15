from sqlalchemy import String, Column, Integer, Boolean, CheckConstraint

from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence.entity.base import Base


class ResultEntity(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_game_board_full = Column(Boolean, nullable=False)

    __table_args__ = (CheckConstraint('length(name) <= 10', name='check_name_length'),)

    def __repr__(self):
        return f"Result [id = {self.id}, name = {self.name}, is_game_board_full = {self.is_game_board_full}]"
