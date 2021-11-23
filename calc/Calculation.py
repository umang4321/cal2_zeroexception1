"""Logic for calculator"""

class Calculation:
    # pylint: disable=too-few-public-methods
    """Calculation class"""
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """Creating Calculation"""
        return cls(value_a, value_b)
