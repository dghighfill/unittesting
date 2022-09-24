
class CalculatorException(Exception):
    """Basic exception for errors raised by Calculator"""
    pass

    def __init__(self, msg=None):
        if msg is None:
            msg = "A Calculator Exception has occurred"

        super(CalculatorException, self).__init__(msg)