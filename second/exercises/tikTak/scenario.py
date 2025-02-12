from axisx import AxisX
from axisy import AxisY
from cell import Cell


class Scenario:
    def __init__(self):
        self.cell_1 = Cell(AxisX.FIRST, AxisY.FIRST, "|___")
        self.cell_2 = Cell(AxisX.FIRST, AxisY.SECOND, "|___")
        self.cell_3 = Cell(AxisX.FIRST, AxisY.THIRD, "|___|")
        self.cell_4 = Cell(AxisX.SECOND, AxisY.FIRST, "|___")
        self.cell_5 = Cell(AxisX.SECOND, AxisY.SECOND, "|___")
        self.cell_6 = Cell(AxisX.SECOND, AxisY.THIRD, "|___|")
        self.cell_7 = Cell(AxisX.THIRD, AxisY.FIRST, "|___")
        self.cell_8 = Cell(AxisX.THIRD, AxisY.SECOND, "|___")
        self.cell_9 = Cell(AxisX.THIRD, AxisY.THIRD, "|___|")

    def display(self):
        print(f"   _{self.cell_1.axis_y.value}_ _{self.cell_2.axis_y.value}_ _{self.cell_3.axis_y.value}_")
        print(f"{self.cell_1.axis_x.value} {self.cell_1.value + self.cell_2.value + self.cell_3.value}")
        print(f"{self.cell_4.axis_x.value} {self.cell_4.value + self.cell_5.value + self.cell_6.value}")
        print(f"{self.cell_7.axis_x.value} {self.cell_7.value + self.cell_8.value + self.cell_9.value}")

    def scenario_validation(self) -> bool:
        for win_sc in self.win_scenarios():
            if win_sc:
                self.display()
                print("=) you won =)")
                return False
        for lose_sc in self.lose_scenarios():
            if lose_sc:
                self.display()
                print("=( you lose =(")
                return False
        return True

    def update(self, current_input: str):
        if self.cell_1.coordinate() == current_input:
            self.cell_1.update_value()
        if self.cell_2.coordinate() == current_input:
            self.cell_2.update_value()
        if self.cell_3.coordinate() == current_input:
            self.cell_3.update_value()
        if self.cell_4.coordinate() == current_input:
            self.cell_4.update_value()
        if self.cell_5.coordinate() == current_input:
            self.cell_5.update_value()
        if self.cell_6.coordinate() == current_input:
            self.cell_6.update_value()
        if self.cell_7.coordinate() == current_input:
            self.cell_7.update_value()
        if self.cell_8.coordinate() == current_input:
            self.cell_8.update_value()
        if self.cell_9.coordinate() == current_input:
            self.cell_9.update_value()

    def win_scenarios(self):
        return (
            (self.cell_1.value == "|_X_" and self.cell_4.value == "|_X_" and self.cell_7.value == "|_X_"),
            (self.cell_2.value == "|_X_" and self.cell_5.value == "|_X_" and self.cell_8.value == "|_X_"),
            (self.cell_3.value == "|_X_|" and self.cell_6.value == "|_X_|" and self.cell_9.value == "|_X_|"),
            (self.cell_1.value == "|_X_" and self.cell_2.value == "|_X_" and self.cell_3.value == "|_X_|"),
            (self.cell_4.value == "|_X_" and self.cell_5.value == "|_X_" and self.cell_6.value == "|_X_|"),
            (self.cell_7.value == "|_X_" and self.cell_8.value == "|_X_" and self.cell_9.value == "|_X_|"),
            (self.cell_1.value == "|_X_" and self.cell_5.value == "|_X_" and self.cell_9.value == "|_X_|"),
            (self.cell_3.value == "|_X_|" and self.cell_5.value == "|_X_" and self.cell_7.value == "|_X_")
        )

    def lose_scenarios(self):
        return (
            (self.cell_1.value == "|_O_" and self.cell_4.value == "|_O_" and self.cell_7.value == "|_O_"),
            (self.cell_2.value == "|_O_" and self.cell_5.value == "|_O_" and self.cell_8.value == "|_O_"),
            (self.cell_3.value == "|_O_|" and self.cell_6.value == "|_O_|" and self.cell_9.value == "|_O_|"),
            (self.cell_1.value == "|_O_" and self.cell_2.value == "|_O_" and self.cell_3.value == "|_O_|"),
            (self.cell_4.value == "|_O_" and self.cell_5.value == "|_O_" and self.cell_6.value == "|_O_|"),
            (self.cell_7.value == "|_O_" and self.cell_8.value == "|_O_" and self.cell_9.value == "|_O_|"),
            (self.cell_1.value == "|_O_" and self.cell_5.value == "|_O_" and self.cell_9.value == "|_O_|"),
            (self.cell_3.value == "|_O_" and self.cell_5.value == "|_O_" and self.cell_7.value == "|_O_")
        )
