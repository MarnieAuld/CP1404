"""
CP1404 Practical 8 - SilverServiceTaxi
Specialised taxi class, derived from Taxi class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string specifically for SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get taxi fare plus flagfall."""
        return super().get_fare() + self.flagfall
