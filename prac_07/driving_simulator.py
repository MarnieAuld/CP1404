"""
Practice and Extension work - Car Driving Simulator
Create a simple menu-driven program
"""
from prac_07.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit
"""


def main():
    """main function"""
    print("Let's Drive!")
    user_car_name = input("Enter your car name: ")
    user_car = Car(user_car_name, 100)
    print(user_car)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            km_to_drive = int(input("How many km do you wish to drive? "))
            while km_to_drive < 0:
                print("Distance must be >= 0")
                km_to_drive = int(input("How many km do you wish to drive? "))
            distance_driven = user_car.drive(km_to_drive)
            print("The car drove {}km".format(distance_driven), end="")
            if user_car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(user_car)
        elif choice == "R":
            refuel_units = int(input("How many units of fuel do you want to add to the car? "))
            while refuel_units < 0:
                print("Fuel amount must be >= 0")
                refuel_units = int(input("How many units of fuel do you want to add to the car? "))
            user_car.add_fuel(refuel_units)
            print("Added {} units of fuel.".format(refuel_units))
            print(user_car)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye {}'s driver,".format(user_car.name))

main()
