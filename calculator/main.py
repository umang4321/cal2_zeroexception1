""" import all the methods from calc_methods"""
from calculator.calculator_calculations.addition import Addition
from calculator.calculator_calculations.subtraction import Subtraction
from calculator.calculator_calculations.multiplication import Multiplication
from calculator.calculator_calculations.division import Division
from calculator.history_calculations.history_calculations import History
from csv_handling.read_csv import CSVRead


class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []
    data = []
    path = ''

    def __init__(self, path):
        self.data = CSVRead.read_data(path)
        self.path = path
        self.move_path = path.replace("input", "done")

    def get_data(self):
        """ Splits the data and returns all columns """
        csv_data = self.data
        num1 = csv_data['num_1'].values
        num2 = csv_data['num_2'].values
        add = [round(i, 3) for i in csv_data['add_nums'].values]
        sub = [round(i, 3) for i in csv_data['sub_nums'].values]
        multi = [round(i, 3) for i in csv_data['mult_nums'].values]
        div = [round(i, 3) for i in csv_data['div_nums'].values]

        return num1, num2, add, sub, multi, div

    @staticmethod
    def add_nums(*args):
        """ Adds given list of numbers and appends the result to history """
        addition = Addition(args).getresult()
        History.add_calculation_to_history(addition)
        return History.get_last_calculation_added()

    @staticmethod
    def subtract_nums(*args):
        """ Subtracts given list of numbers and appends the result to history """
        subtraction = Subtraction(args).getresult()
        History.add_calculation_to_history(subtraction)
        return History.get_last_calculation_added()

    @staticmethod
    def multiply_nums(*args):
        """ Multiplies given list of numbers and appends the result to history """
        multiplication = Multiplication(args).getresult()
        History.add_calculation_to_history(multiplication)
        return History.get_last_calculation_added()

    @staticmethod
    def divide_nums(*args):
        """ Divides given list of numbers and appends the result to history """
        division = Division(args).getresult()
        History.add_calculation_to_history(division)
        return History.get_last_calculation_added()
