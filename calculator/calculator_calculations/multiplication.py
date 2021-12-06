"""Multiplication Class"""

from calculator.calculator_calculations.calculation import Calculation

# This is multiplication method which inherits the calculation class constructor


class Multiplication(Calculation):
    """Calculation Multiplication Class"""

    def getresult(self):
        """Get multiplication results"""
        multiplication_of_values = 1
        for value in self.values:
            multiplication_of_values = multiplication_of_values * value
        return round(multiplication_of_values, 3)
