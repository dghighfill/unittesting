from exceptions import CalculatorException
class Calculator:

    def __init__(self):
        self.__on: bool = False

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

