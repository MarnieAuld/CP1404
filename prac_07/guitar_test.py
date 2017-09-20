"""
Do-from-scratch Exercises - Guitars
Test class functionality
"""
from prac_07.guitar import Guitar

GIBSON_EXPECTED_AGE = 95
ANOTHER_GUITAR_EXPECTED_AGE = 5


def main():
    """......"""
    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    Another_Guitar = Guitar("Another Guitar", 2012, 2300.10)

    print("{} get_age() - Expected {}. Got {}".format(Gibson.name, GIBSON_EXPECTED_AGE, Gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(Another_Guitar.name, ANOTHER_GUITAR_EXPECTED_AGE, Another_Guitar.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(Gibson.name, "True", Gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(Another_Guitar.name, "False", Another_Guitar.is_vintage()))

main()