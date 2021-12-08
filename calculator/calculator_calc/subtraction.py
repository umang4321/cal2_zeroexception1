"""Subtraction Class"""

from calculator.calculator_calc.calculation import Calculation

# This is subtraction method which inherits the calculation class constructor


class Subtraction(Calculation):
    """Calculation Subtraction class"""

    def getresult(self):
        """Get subtraction results"""
        subtraction_of_values = self.values[0]
        for value in self.values[1:]:
            subtraction_of_values = subtraction_of_values - value
        return round(subtraction_of_values, 3)
