""" This is the increment function"""
from calculator.calculator_calculations.addition import Addition
from calculator.calculator_calculations.subtraction import Subtraction
from calculator.calculator_calculations.multiplication import Multiplication
from calculator.calculator_calculations.division import Division
from calculator.history_calculations.history_calculations import History
from csv_file.read_csv import CSVRead


class Calculator:
    """ This is the Calculator class"""
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
        """returns object of the addition result of the numbers"""
        addition = Addition(args).getresult()
        History.add_calculation_to_history(addition)
        return History.get_last_calculation_added()

    @staticmethod
    def subtract_nums(*args):
        """returns object of the subtraction result of the numbers"""
        subtraction = Subtraction(args).getresult()
        History.add_calculation_to_history(subtraction)
        return History.get_last_calculation_added()

    @staticmethod
    def multiply_nums(*args):
        """ returns object of the multiplication result of the numbers"""
        multiplication = Multiplication(args).getresult()
        History.add_calculation_to_history(multiplication)
        return History.get_last_calculation_added()

    @staticmethod
    def divide_nums(*args):
        """returns object of the division result of the numbers"""
        division = Division(args).getresult()
        History.add_calculation_to_history(division)
        return History.get_last_calculation_added()
