import unittest

from second.exercises.tikTak.domain.axis_x import AxisX
from second.exercises.tikTak.domain.cell import Cell
from second.exercises.tikTak.domain.play_symbol import PlaySymbol


class CellTest(unittest.TestCase):

    def test_is_free_true(self):
        cell = Cell(AxisX.FIRST.value, AxisX.FIRST.value, "|___")

        result = cell.is_free()

        self.assertTrue(result)

    def test_is_free_x_false(self):
        cell = Cell(AxisX.FIRST.value, AxisX.FIRST.value, "|_X_")

        result = cell.is_free()

        self.assertFalse(result)

    def test_is_free_o_false(self):
        cell = Cell(AxisX.FIRST.value, AxisX.FIRST.value, "|_O_")

        result = cell.is_free()

        self.assertFalse(result)

    def test_update_value_true(self):
        cell = Cell(AxisX.FIRST.value, AxisX.FIRST.value, "|___")
        new_value = PlaySymbol.symbol_x.value

        result = cell.update_value(new_value)

        self.assertTrue(result)
        self.assertEqual(cell.value[2], new_value)

    def test_update_value_false(self):
        cell = Cell(AxisX.FIRST.value, AxisX.FIRST.value, "|_O_")
        new_value = PlaySymbol.symbol_x.value

        result = cell.update_value(new_value)

        self.assertFalse(result)
        self.assertNotEqual(cell.value[2], new_value)
