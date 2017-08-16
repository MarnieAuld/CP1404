# def name_getter():
#     name = input("Enter your name: ")
#     while name == "":
#         print("Invalid input - Please try again")
#         name = input("Enter your name: ")
#
#     print(name[::2])


def main():
    name = get_name()
    print_parts(name)


def print_parts(name, frequency=2):
    print(name[::frequency])


def get_name():
    name = input("Enter your name: ")
    while name == "":
        print("Invalid input - Please try again")
        name = input("Enter your name: ")
    return name


main()