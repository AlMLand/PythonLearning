from cell import Cell


class Row:
    def __init__(self, cell_1: Cell, cell_2: Cell, cell_3: Cell):
        self.cell_1 = cell_1
        self.cell_2 = cell_2
        self.cell_3 = cell_3

    def get_all_cells(self) -> list[Cell]:
        return [self.cell_1, self.cell_2, self.cell_3]

    def display(self):
        print(f"{self.cell_1.axis_x.value} {self.cell_1.value + self.cell_2.value + self.cell_3.value}")
