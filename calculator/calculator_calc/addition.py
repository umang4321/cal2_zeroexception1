"""Addition Class"""
from calculator.calculator_calc.calculation import Calculation

# This is addition method which inherits the calculation class constructor


class Addition(Calculation):
    """ Calculation addition class"""

    def getresult(self):
        """Get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = sum_of_values + value
        return round(sum_of_values, 3)
