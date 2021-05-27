import pytest
import unittest

from CalcTask import CalcTask

class Calctest_task(unittest.TestCase):

    calc = CalcTask()
# this will run first (should pass)
    def test_percentage(self): # naming convention is essential as 'test' is the word we need to use naming tests
        self.assertEqual(self.calc.percentage(25, 100), 25) # it will add them and check if it is 6

    def test_is_number_divisible(self):
        self.assertEqual(self.calc.is_number_divisible(11, 5), False)

    def test_cm_to_inches(self):
        self.assertEqual(self.calc.cm_to_inches(1), 0.39370079)

    def test_area_of_triangle(self):
        self.assertEqual(self.calc.area_of_triangle(10, 2), 10)

