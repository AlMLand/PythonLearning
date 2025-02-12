from cell import Cell
from column import Column
from row import Row


class Scenario:
    def __init__(self):
        self.cell_1 = Cell(Row.FIRST, Column.FIRST, "|___")
        self.cell_2 = Cell(Row.FIRST, Column.SECOND, "|___")
        self.cell_3 = Cell(Row.FIRST, Column.THIRD, "|___|")
        self.cell_4 = Cell(Row.SECOND, Column.FIRST, "|___")
        self.cell_5 = Cell(Row.SECOND, Column.SECOND, "|___")
        self.cell_6 = Cell(Row.SECOND, Column.THIRD, "|___|")
        self.cell_7 = Cell(Row.THIRD, Column.FIRST, "|___")
        self.cell_8 = Cell(Row.THIRD, Column.SECOND, "|___")
        self.cell_9 = Cell(Row.THIRD, Column.THIRD, "|___|")

    def get_scenario(self):
        return (
            self.cell_1.get_cell(), self.cell_2.get_cell(), self.cell_3.get_cell(), self.cell_4.get_cell(),
            self.cell_5.get_cell(), self.cell_6.get_cell(), self.cell_7.get_cell(), self.cell_8.get_cell(),
            self.cell_9.get_cell()
        )

    def display(self):
        print(f"   _{self.cell_1.column.value}_ _{self.cell_2.column.value}_ _{self.cell_3.column.value}_")
        print(f"{self.cell_1.row.value} {self.cell_1.value + self.cell_2.value + self.cell_3.value}")
        print(f"{self.cell_4.row.value} {self.cell_4.value + self.cell_5.value + self.cell_6.value}")
        print(f"{self.cell_7.row.value} {self.cell_7.value + self.cell_8.value + self.cell_9.value}")

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
            self.cell_1.value = self.update_value(self.cell_1.value)
        if self.cell_2.coordinate() == current_input:
            self.cell_2.value = self.update_value(self.cell_2.value)
        if self.cell_3.coordinate() == current_input:
            self.cell_3.value = self.update_value(self.cell_3.value)
        if self.cell_4.coordinate() == current_input:
            self.cell_4.value = self.update_value(self.cell_4.value)
        if self.cell_5.coordinate() == current_input:
            self.cell_5.value = self.update_value(self.cell_5.value)
        if self.cell_6.coordinate() == current_input:
            self.cell_6.value = self.update_value(self.cell_6.value)
        if self.cell_7.coordinate() == current_input:
            self.cell_7.value = self.update_value(self.cell_7.value)
        if self.cell_8.coordinate() == current_input:
            self.cell_8.value = self.update_value(self.cell_8.value)
        if self.cell_9.coordinate() == current_input:
            self.cell_9.value = self.update_value(self.cell_9.value)

    def update_value(self, value: str):
        return "".join([c if i != 2 else "X" for i, c in enumerate(value)])

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
