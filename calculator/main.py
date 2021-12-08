""" This is the increment function"""
import logging
import sys

from calculator.calculator_calc.addition import Addition
from calculator.calculator_calc.subtraction import Subtraction
from calculator.calculator_calc.multiplication import Multiplication
from calculator.calculator_calc.division import Division
from calculator.history_calc.history_calculations import History
from csv_file.read_csv import CSVRead

sys.tracebacklimit = 0
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

filecalc_handler = logging.FileHandler('log/calculation.log')
filecalc_handler.setLevel(logging.DEBUG)
filecalc_handler.setFormatter(formatter)

streamcalc_handler = logging.StreamHandler()
streamcalc_handler.setFormatter(formatter)

logger.addHandler(filecalc_handler)
logger.addHandler(streamcalc_handler)

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
        try:
            division = Division(args).getresult()
            History.add_calculation_to_history(division)
        except ZeroDivisionError as err:
            logger.exception(err)
            return 0.0
        else:
            logger.debug('Division : %f / %f = %f', args[0], args[1], division)
            return History.get_last_calculation_added()
