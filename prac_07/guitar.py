"""
Do-from-scratch Exercises - Guitars
Store guitar attributes in Guitar class.
"""

CURRENT_YEAR = 2017
VINTAGE_YEAR = 50


class Guitar:
    """Guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar.
        name: string name for guitar (make AND model)
        year: int - guitar manufacture year
        cost: float - cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Returns how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        # """Determines whether the guitar is more than 50 years old and returns TRUE or FALSE"""
        return self.get_age() >= VINTAGE_YEAR
        # if self.get_age() >= VINTAGE_YEAR:
        #     return self.is_vintage == "vintage"
