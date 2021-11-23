"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ Calculation division class"""
    def get_result(self):
        """Get division results"""
        result = 1.0
        for value in self.values:
            result = value/result
        return result
