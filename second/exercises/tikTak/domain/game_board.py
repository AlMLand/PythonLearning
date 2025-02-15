from second.exercises.tikTak.domain.axis_x import AxisX
from second.exercises.tikTak.domain.axis_y import AxisY
from second.exercises.tikTak.domain.cell import Cell
from second.exercises.tikTak.domain.row import Row


class GameBoard:
    def __init__(self):
        self.row_1 = Row(
            Cell(AxisX.FIRST, AxisY.FIRST, "|___"), Cell(AxisX.FIRST, AxisY.SECOND, "|___"),
            Cell(AxisX.FIRST, AxisY.THIRD, "|___|")
        )
        self.row_2 = Row(
            Cell(AxisX.SECOND, AxisY.FIRST, "|___"), Cell(AxisX.SECOND, AxisY.SECOND, "|___"),
            Cell(AxisX.SECOND, AxisY.THIRD, "|___|")
        )
        self.row_3 = Row(
            Cell(AxisX.THIRD, AxisY.FIRST, "|___"), Cell(AxisX.THIRD, AxisY.SECOND, "|___"),
            Cell(AxisX.THIRD, AxisY.THIRD, "|___|")
        )

    def is_free_space_available(self) -> bool:
        return (self.row_1.is_free_cell_available()
                or self.row_2.is_free_cell_available() or self.row_3.is_free_cell_available())

    def identical_r1c1_r2c1_r3c2_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_1.cell_1.value == new_value_1
                and self.row_2.cell_1.value == new_value_2 and self.row_3.cell_1.value == new_value_3)

    def identical_r1c2_r2c2_r3c2_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_1.cell_2.value == new_value_1
                and self.row_2.cell_2.value == new_value_2 and self.row_3.cell_2.value == new_value_3)

    def identical_r1c3_r2c3_r3c3_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_1.cell_3.value == new_value_1
                and self.row_2.cell_3.value == new_value_2 and self.row_3.cell_3.value == new_value_3)

    def identical_r1c1_r1c2_r1c3_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_1.cell_1.value == new_value_1
                and self.row_1.cell_2.value == new_value_2 and self.row_1.cell_3.value == new_value_3)

    def identical_r2c1_r2c2_r2c3_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_2.cell_1.value == new_value_1
                and self.row_2.cell_2.value == new_value_2 and self.row_2.cell_3.value == new_value_3)

    def identical_r3c1_r3c2_r3c3_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_3.cell_1.value == new_value_1
                and self.row_3.cell_2.value == new_value_2 and self.row_3.cell_3.value == new_value_3)

    def identical_r1c1_r2c2_r3c3_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_1.cell_1.value == new_value_1
                and self.row_2.cell_2.value == new_value_2 and self.row_3.cell_3.value == new_value_3)

    def identical_r1c3_r2c2_r3c1_values(self, new_value_1: str, new_value_2: str, new_value_3: str) -> bool:
        return (self.row_1.cell_3.value == new_value_1
                and self.row_2.cell_2.value == new_value_2 and self.row_3.cell_1.value == new_value_3)

    def get_all_rows(self) -> list[Row]:
        return [self.row_1, self.row_2, self.row_3]

    def display(self):
        print(
            f"   _{self.row_1.cell_1.axis_y.value}_ _{self.row_2.cell_2.axis_y.value}_ _{self.row_3.cell_3.axis_y.value}_")
        self.row_1.display()
        self.row_2.display()
        self.row_3.display()

    def update_board(self, current_input: str, symbol: str):
        if self.row_1.cell_1.coordinate() == current_input and self.row_1.cell_1.is_free():
            return self.row_1.cell_1.update_value(symbol)
        elif self.row_1.cell_2.coordinate() == current_input and self.row_1.cell_2.is_free():
            return self.row_1.cell_2.update_value(symbol)
        elif self.row_1.cell_3.coordinate() == current_input and self.row_1.cell_3.is_free():
            return self.row_1.cell_3.update_value(symbol)
        elif self.row_2.cell_1.coordinate() == current_input and self.row_2.cell_1.is_free():
            return self.row_2.cell_1.update_value(symbol)
        elif self.row_2.cell_2.coordinate() == current_input and self.row_2.cell_2.is_free():
            return self.row_2.cell_2.update_value(symbol)
        elif self.row_2.cell_3.coordinate() == current_input and self.row_2.cell_3.is_free():
            return self.row_2.cell_3.update_value(symbol)
        elif self.row_3.cell_1.coordinate() == current_input and self.row_3.cell_1.is_free():
            return self.row_3.cell_1.update_value(symbol)
        elif self.row_3.cell_2.coordinate() == current_input and self.row_3.cell_2.is_free():
            return self.row_3.cell_2.update_value(symbol)
        elif self.row_3.cell_3.coordinate() == current_input and self.row_3.cell_3.is_free():
            return self.row_3.cell_3.update_value(symbol)
        else:
            return False
