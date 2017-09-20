"""
Do-from-scratch Exercises - Guitars
Test class functionality
"""
from prac_07.guitar import Guitar

GIBSON_EXPECTED_AGE = 95
ANOTHER_GUITAR_EXPECTED_AGE = 5


def main():
    """Test functionality of Guitar Class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 2300.10)
    print(gibson)
    print(another_guitar)
    print()
    print("{} get_age() - Expected {}. Got {}".format(gibson.name, GIBSON_EXPECTED_AGE, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".
          format(another_guitar.name, ANOTHER_GUITAR_EXPECTED_AGE, another_guitar.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, "True", gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, "False", another_guitar.is_vintage()))


main()
