"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print("{} is {}".format(state, STATE_NAMES[state]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

"""
string formatting state names in a loop
"""
for state_name in STATE_NAMES:
    print("{:3} is {}".format(state_name, STATE_NAMES[state_name]))
