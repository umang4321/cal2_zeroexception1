"""Subtraction Class"""

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """Calculation Subtraction class"""
    def get_result(self):
        """Get subtraction results"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values =   difference_of_values - value
        return difference_of_values
