from cell import Cell
from play_symbol import PlaySymbol


class Row:
    def __init__(self, cell_1: Cell, cell_2: Cell, cell_3: Cell):
        self.cell_1 = cell_1
        self.cell_2 = cell_2
        self.cell_3 = cell_3

    def is_free_cell_available(self):
        return (self._is_not_in(self.cell_1.value)
                or self._is_not_in(self.cell_2.value) or self._is_not_in(self.cell_3.value))

    def _is_not_in(self, cell_value: str) -> bool:
        return PlaySymbol.symbol_o.value not in cell_value and PlaySymbol.symbol_x.value not in cell_value

    def get_all_cells(self) -> list[Cell]:
        return [self.cell_1, self.cell_2, self.cell_3]

    def display(self):
        print(f"{self.cell_1.axis_x.value} {self.cell_1.value + self.cell_2.value + self.cell_3.value}")
