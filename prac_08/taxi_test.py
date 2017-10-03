"""
CP1404 Practical 8 - TAXI
1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
2. Drive the taxi 40km
3. Print the taxi's details and the current fare
4. Restart the meter (start a new fare) and then drive the car 100km
5. Print the details and the current fare
"""

from prac_08.taxi import Taxi


def main():
    """Test code for Taxi class."""
    taxi = Taxi("Prius 1", 100)
    taxi.start_fare()
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)

main()
