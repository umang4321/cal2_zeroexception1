""" This is the increment function"""


class Calculator:
    """ initialization 0 for result """

    def __init__(self):
        pass

    result = 0

    def get_result(self):
        """ Defining result function"""
        return self.result

    def add_number(self, value_a):
        """ Defining addition function"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ Defining subtraction function"""
        self.result = self.result - value_a
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """ Defining division function"""
        self.result = value_a * value_b
        return self.result

    def divide_numbers(self, value_a, value_b):
        """ Defining division function"""
        try:
            self.result = (value_a / value_b)
            # returns the result
            return self.result
        except ZeroDivisionError:
            return 0
