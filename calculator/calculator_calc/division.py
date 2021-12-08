"""Division Class"""

from calculator.calculator_calc.calculation import Calculation

# This is division method which inherits the calculation class constructor


class Division(Calculation):
    """ Calculation division class"""

    def getresult(self):
        """Get division results"""
        division_of_values = self.values[0]
        for value in self.values[1:]:
            division_of_values = division_of_values / value
        return round(division_of_values, 3)
