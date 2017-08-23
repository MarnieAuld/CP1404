""" import random
user input for number of quick picks, while loop for error checking < 0
print number of quick picks in blocks of 6 NUMBERS, MINIMUM_NUMBER = 1, MAXIMUM_NUMBER = 45
"""

import random


def main():

    number_of_tickets = int(input("How many Quick Picks? "))
    while number_of_tickets < 0:
        print("Invalid Input")
        number_of_tickets = int(input("How many Quick Picks? "))


    number = random.randint(1, 45)
    print(number)


main()





