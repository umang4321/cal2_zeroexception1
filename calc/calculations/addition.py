"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ Calculation addition class"""
    def get_result(self):
        """Get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
