from second.exercises.tikTak.domain.axis_x import AxisX
from second.exercises.tikTak.domain.axis_y import AxisY
from second.exercises.tikTak.domain.play_symbol import PlaySymbol


class Cell:
    def __init__(self, axis_x: AxisX, axis_y: AxisY, value: str):
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.value = value

    def is_free(self) -> bool:
        return PlaySymbol.symbol_o.value not in self.value and PlaySymbol.symbol_x.value not in self.value

    def update_value(self, symbol: str) -> bool:
        if self.is_free():
            self.value = "".join([character if index != 2 else symbol for index, character in enumerate(self.value)])
            return True
        else:
            return False

    def coordinate(self):
        return f"{self.axis_x.value}{self.axis_y.value}"

    def get_cell(self):
        return [f"{self.axis_x.value}{self.axis_y.value}", f"{self.value.value}"]
