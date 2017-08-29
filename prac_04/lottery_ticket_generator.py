"""
import random
user input for number of quick picks, while loop for error checking < 0
create empty list (quickpick)
append random number to quickpick list, check for number in list already (while number in quickpick)
quickpick.sort()
print number of quick picks in blocks of 6 NUMBERS, MINIMUM_NUMBER = 1, MAXIMUM_NUMBER = 45
check
"""

import random


def main():
    number_of_tickets = int(input("How many Quick Picks? "))
    while number_of_tickets < 0:
        print("Invalid Input")
        number_of_tickets = int(input("How many Quick Picks? "))

    for number in range(number_of_tickets):
        quick_pick = []
        for i in range(6):
            number = random.randint(1, 45)
            while number in quick_pick:
                number = random.randint(1, 45)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:3}".format(number) for number in quick_pick))

main()



#   my attempt -    print("{:3}".format(quick_pick) for number in quick_pick)
