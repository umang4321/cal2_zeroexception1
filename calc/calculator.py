""" This is the increment function"""
from calc.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        """ returns the last result value of calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """returns object of the addition result of the numbers"""
        return Calculations.add_addition_calculation(tuple_values)

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """returns object of the subtraction result of the numbers"""
        return Calculations.add_subtraction_calculation(tuple_values)

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ returns object of the multiplication result of the numbers"""
        return Calculations.add_multiplication_calculation(tuple_values)

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """returns object of the division result of the numbers"""
        return Calculations.add_division_calculation(tuple_values)
