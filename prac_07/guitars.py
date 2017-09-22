"""
Do-from-scratch Exercises - Playing the Guitars
Store user's guitars until blank input
Print their details in the following format:
"These are my guitars:
Guitar 1: Fender Stratocaster (2014),  worth $    765.40
Guitar 2:      Gibson L-5 CED (1922),  worth $ 16,035.40  (vintage)
Guitar 3:       Line 6 JTV-59 (2010),  worth $  1,512.90
"""
from prac_07.guitar import Guitar


def main():
    """Print output to match sample output"""
    guitars = [Guitar("Fender Stratocaster", 2014, 765.40), Guitar("Gibson L-5 CES", 1922, 16035.40),
               Guitar("Line 6 JTV-59", 2010, 1512.90)]
    for i, guitar in enumerate(guitars):
        # TODO: replace next 4 lines with ternary operator
        # if guitar.is_vintage():
        #     vintage_string = "(vintage)"
        # else:
        #     vintage_string = ""
        vintage_string = "(vintage)" if guitar.is_vintage() else ""

        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".
              format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
        # print("Guitar {}: {self.name} ({self.year}), worth ${self.cost}".format(i+1, self = guitar))
        # Can you use placeholders if you have format variables outside self - and how do you string format


main()
