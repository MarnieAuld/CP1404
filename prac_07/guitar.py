"""
Do-from-scratch Exercises - Guitars
Store guitar attributes in Guitar class.
"""


class Guitar:
    """Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar.
        name: string name for guitar (make AND model)
        year: int - guitar manufacture year
        cost: float - cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost