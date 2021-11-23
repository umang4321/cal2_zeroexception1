"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    mynumbers = (1.0, 2.0)
    divide = Division(mynumbers)
    assert divide.get_result() == 2.0
