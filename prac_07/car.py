"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Car object."""
    def __init__(self, name="", fuel=0):
        """Initialise a car instance.
        name: string name for car
        fuel: integer value
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string"""
        return "{}, fuel= {}, odometer= {}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """Add amount to the fuel total."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a specified distance.
        If car has enough fuel, drive distance
        Else drive until fuel = 0
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
