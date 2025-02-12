from axisx import AxisX
from axisy import AxisY
from cell import Cell
from row import Row


class Scenario:
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

    def display(self):
        print(
            f"   _{self.row_1.cell_1.axis_y.value}_ _{self.row_2.cell_2.axis_y.value}_ _{self.row_3.cell_3.axis_y.value}_")
        self.row_1.display()
        self.row_2.display()
        self.row_3.display()

    def winning(self) -> bool:
        for win_sc in self._win_scenarios():
            if win_sc:
                self.display()
                print("=) you won =)")
                return False
        for lose_sc in self._lose_scenarios():
            if lose_sc:
                self.display()
                print("=( you lose =(")
                return False
        return True

    def update(self, current_input: str, symbol: str):
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

    def _win_scenarios(self):
        return (
            (self.row_1.cell_1.value == "|_X_" and self.row_2.cell_1.value == "|_X_"
             and self.row_3.cell_1.value == "|_X_"),
            (self.row_1.cell_2.value == "|_X_" and self.row_2.cell_2.value == "|_X_"
             and self.row_3.cell_2.value == "|_X_"),
            (self.row_1.cell_3.value == "|_X_|" and self.row_2.cell_3.value == "|_X_|"
             and self.row_3.cell_3.value == "|_X_|"),
            (self.row_1.cell_1.value == "|_X_" and self.row_1.cell_2.value == "|_X_"
             and self.row_1.cell_3.value == "|_X_|"),
            (self.row_2.cell_1.value == "|_X_" and self.row_2.cell_2.value == "|_X_"
             and self.row_2.cell_3.value == "|_X_|"),
            (self.row_3.cell_1.value == "|_X_" and self.row_3.cell_2.value == "|_X_"
             and self.row_3.cell_3.value == "|_X_|"),
            (self.row_1.cell_1.value == "|_X_" and self.row_2.cell_2.value == "|_X_"
             and self.row_3.cell_3.value == "|_X_|"),
            (self.row_1.cell_3.value == "|_X_|" and self.row_2.cell_2.value == "|_X_"
             and self.row_3.cell_1.value == "|_X_")
        )

    def _lose_scenarios(self):
        return (
            (self.row_1.cell_1.value == "|_O_" and self.row_2.cell_1.value == "|_O_"
             and self.row_3.cell_1.value == "|_O_"),
            (self.row_1.cell_2.value == "|_O_" and self.row_2.cell_2.value == "|_O_"
             and self.row_3.cell_2.value == "|_O_"),
            (self.row_1.cell_3.value == "|_O_|" and self.row_2.cell_3.value == "|_O_|"
             and self.row_3.cell_3.value == "|_O_|"),
            (self.row_1.cell_1.value == "|_O_" and self.row_1.cell_2.value == "|_O_"
             and self.row_1.cell_3.value == "|_O_|"),
            (self.row_2.cell_1.value == "|_O_" and self.row_2.cell_2.value == "|_O_"
             and self.row_2.cell_3.value == "|_O_|"),
            (self.row_3.cell_1.value == "|_O_" and self.row_3.cell_2.value == "|_O_"
             and self.row_3.cell_3.value == "|_O_|"),
            (self.row_1.cell_1.value == "|_O_" and self.row_2.cell_2.value == "|_O_"
             and self.row_3.cell_3.value == "|_O_|"),
            (self.row_1.cell_3.value == "|_O_|" and self.row_2.cell_2.value == "|_O_"
             and self.row_3.cell_1.value == "|_O_")
        )
