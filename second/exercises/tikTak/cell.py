from axisx import AxisX
from axisy import AxisY


class Cell:
    def __init__(self, axis_x: AxisX, axis_y: AxisY, value: str):
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.value = value

    def update_value(self, symbol: str):
        self.value = "".join([character if index != 2 else symbol for index, character in enumerate(self.value)])

    def coordinate(self):
        return f"{self.axis_x.value}{self.axis_y.value}"

    def get_cell(self):
        return [f"{self.axis_x.value}{self.axis_y.value}", f"{self.value.value}"]
