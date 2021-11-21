""" This is the increment function"""
#first import the addition namespace
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""
    #this is the calculator static property
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """First Calculation"""
        return Calculator.history[0].getresult()
    @staticmethod
    def clear_history():
        """Clear History"""
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        """History count"""
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        """Add calculation to history"""
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Last calculation"""
        return Calculator.history[-1].getresult()
    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    #this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        # create an subtraction object using the factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def division_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
