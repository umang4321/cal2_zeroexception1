"""Logic for calculator"""
class Calculation:
    # pylint: disable=too-few-public-methods
    """Calculation class"""
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
    # Class Factory Method <- bound to the class and not the instance of the class

    @classmethod
    def create(cls, value_a, value_b):
        """Performing Calculation"""
        return cls(value_a, value_b)
