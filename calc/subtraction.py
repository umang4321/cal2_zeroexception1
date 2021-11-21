"""Subtraction method"""
from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def getresult(self):
        """Division method"""
        return self.value_a - self.value_b
