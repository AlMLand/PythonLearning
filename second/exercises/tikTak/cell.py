from column import Column
from row import Row


class Cell:
    def __init__(self, row: Row, column: Column, value: str):
        self.row = row
        self.column = column
        self.value = value

    def coordinate(self):
        return f"{self.row.value}{self.column.value}"

    def get_cell(self):
        return [f"{self.row.value}{self.column.value}", f"{self.value.value}"]
