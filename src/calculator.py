from exceptions import CalculatorException, NumberFormatException

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

    def get_numbers(self):
        return self.__numbers

    def add(self, value: int):
        if self.is_on():
            self.__numbers.append(value)
        else:
            raise CalculatorException("Power must be turned on")

    def add_numbers(self, numbers: list):
        if self.is_on():
            self.__numbers .extend(numbers)
        else:
            raise CalculatorException()

    def equals(self):
        total: int = 0
        for value in self.get_numbers():
            if isinstance(value, int):
                total = total + value
            else:
                raise NumberFormatException
        return total
