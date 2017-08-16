# def version_1():
#     """Get name thing, without functions."""
#     name = input("Enter your name: ")
#     while name == "":
#         print("Invalid input - Please try again.")
#         name = input("Enter your name: ")
#
#     print(name[::2])


def main():
    name = get_name()
    print_parts(name, 2)


def print_parts(name, step=0):
    print(name[::step])


def get_name():
    name = input("Enter your name: ")
    while name == "":
        print("Invalid input - Please try again.")
        name = input("Enter your name: ")
    return name


main()
