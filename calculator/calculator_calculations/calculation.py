"""Calculation Class"""


class Calculation:
    """ calculation abstract base class"""

    # pylint: disable=too-few-public-methods

    def __init__(self, values: tuple):
        # Calls the function to convert given values to float and returns the values as tuples
        self.values = Calculation.convert_args_to_list_float(values)

    # Class Factory Method
    @staticmethod
    def convert_args_to_list_float(values):
        """ Returns the list of float values back """
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
