"""
Print requested hexadecimal colours in a dictionary
"""

COLOUR_NAMES = {"MINTGREEN": "#f5fffa", "VIOLET": "#ee82ee", "STEELBLUE": "#4682b4", "SANDYBROWN": "#f4a460",
                "PALEGREEN": "#98fb98", "ORCHID": "#da70d6", "NAVYBLUE": "#000080", "MAGENTA": "#ff00ff",
                "LIMEGREEN": "#32cd32", "HOTPINK": "#ff69b4", "FIREBRICK": "#b22222"}

user_colour = str(input("Enter colour name: ").upper().replace(" ", ""))
while user_colour != "":
    if user_colour in COLOUR_NAMES:
        print("Hexadecimal code for {} is:  {}".format(user_colour, COLOUR_NAMES[user_colour]))
    else:
        print("Invalid colour name")
    user_colour = str(input("Enter colour name: ").upper().replace(" ", ""))
