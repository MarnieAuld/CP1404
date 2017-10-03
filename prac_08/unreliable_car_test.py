"""
CP1404 Practical 8 - UNRELIABLE CAR TEST
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test one high reliability and one low reliability car"""
    highly_reliable_car = UnreliableCar("Good Car", 100, 80)
    lowly_reliable_car = UnreliableCar("Bad Car", 100, 20)

    for i in range(1, 20, 2):
        print("{:8} attempted to drive {:2}km - Managed to drive: {:2}km"
              .format(highly_reliable_car.name, i, highly_reliable_car.drive(i)))
        print("{:8} attempted to drive {:2}km - Managed to drive: {:2}km"
              .format(lowly_reliable_car.name, i, lowly_reliable_car.drive(i)))
        print()
    print(highly_reliable_car)
    print(lowly_reliable_car)
main()
