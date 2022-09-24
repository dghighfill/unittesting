# To run this test from the src directory enter the following on the command line
# python -m unittest tests/test_calculator.py

import unittest
from calculator import Calculator
from exceptions import CalculatorException
from hamcrest import has_items, assert_that, equal_to


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
        self.calc.add(2)
        assert_that(self.calc.equals(), equal_to(2))

    def test_wont_add_without_power(self):
        with self.assertRaises(CalculatorException) as context:
            response = self.calc.add(2)

        self.assertEquals(str(context.exception), "Power must be turned on")

    def test_add_single_value(self):
        self.calc.power_on()
        self.calc.add(2)
        assert_that(self.calc.get_numbers(), has_items(2))

    def test_add_multiple_values(self):
        self.calc.power_on()
        self.calc.add(2)
        self.calc.add(2)
        self.calc.add(10)
        assert_that(self.calc.equals(), equal_to(14))

    def test_add_single_value_with_negative(self):
        self.calc.power_on()
        self.calc.add(2)
        self.calc.add(-2)
        self.calc.add(10)
        assert_that(self.calc.equals(), equal_to(10))

    def test_add_list_of_numbers(self):
        self.calc.power_on()
        self.calc.add_numbers([2, -2, 10, 5])
        assert_that(self.calc.equals(), equal_to(15))