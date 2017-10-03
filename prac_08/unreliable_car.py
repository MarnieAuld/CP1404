"""
CP1404 Practical 8 - UNRELIABLE CAR
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise the unreliable car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the unreliable car, depending on reliability"""
        distance_driven = 0
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
