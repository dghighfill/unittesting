from exceptions import CalculatorException


class Calculator:

    def __init__(self):
        self.__on: bool = False
        self.__numbers: list = []

    def is_on(self):
        return self.__on

    def power_on(self):
        self.__on = True

    def power_off(self):
        self.__on = False

    def add(self, value1: int, value2: int):
        if self.is_on():
            return value1+value2
        else:
            raise CalculatorException("Power must be turned on")

    def get_numbers(self):
        return self.__numbers

    def add_number(self, value: int):
        if self.is_on():
            self.__numbers.append(value)
        else:
            raise CalculatorException("Power must be turned on")

    def equals(self):
        total: int = 0
        for value in self.get_numbers():
            total = total + value
        return total
