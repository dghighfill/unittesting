# To run this test from the src directory enter the following on the command line
# python -m unittest tests/test_calculator.py

import unittest
from calculator import Calculator
from exceptions import CalculatorException


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc: Calculator = Calculator()

    def test_constructor(self):
        self.assertFalse(self.calc.is_on())

    def test_power_on(self):
        self.calc.power_on()
        self.assertTrue(self.calc.is_on())

    def test_power_off(self):
        self.calc.power_off()
        self.assertFalse(self.calc.is_on())

    def test_add(self):
        self.calc.power_on()
        response = self.calc.add(2, 2)
        self.assertEquals(response, 4)

    def test_wont_add_without_power(self):
        with self.assertRaises(CalculatorException) as context:
            response = self.calc.add(2, 2)

        self.assertEquals(str(context.exception), "Power must be turned on")





