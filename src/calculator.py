
class Calculator:

    def __init__(self):
        self.__on: bool = False

    def is_on(self):
        return self.__on

    def power_on(self):
        self.__on = True

    def power_off(self):
        self.__on = False
