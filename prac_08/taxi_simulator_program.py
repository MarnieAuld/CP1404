"""
CP1404 Practical 8 - Taxi Simulator Program
Write a taxi simulator program that uses your Taxi and SilverService Taxi classes
Each time, until they quit:
The user should be presented with a list of available taxis and get to choose one.
Then they can choose how far they want to drive,
At the end of each trip, show them the trip cost and add it to their bill.
"""


from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi
from prac_08.car import Car

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
number_of_available_taxis = len(taxis)
MENU = """q)uit,
c)hoose taxi,
d)rive
"""


def main():
    total_trip_cost = 0
    print("Lets drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis Available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > len(taxis):
                print("Invalid Input - Try Again")
                print(MENU)
                menu_choice = input(">>> ").upper()
            chosen_taxi = taxis[taxi_choice]
        elif menu_choice == "D":
            chosen_taxi.start_fare()
            distance_to_drive = input("Drive how far? ")
            chosen_taxi.drive(distance_to_drive)
            single_trip_cost = chosen_taxi.get_fare()
            print("Your {} trip cost you ${:2f}".format(chosen_taxi.name, single_trip_cost))
            total_trip_cost += single_trip_cost
        else:
            print("Invalid option")
        print( "Bill to date: ${:.2f}".format(total_trip_cost))
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_trip_cost))
    print("Taxis are now: ")
    display_taxis(taxis)


main()
