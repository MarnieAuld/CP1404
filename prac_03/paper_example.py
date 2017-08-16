def main():

    name = get_name()

    print(name[::2])


def get_name():
    name = input("Enter your name: ")
    while name == "":
        print("Invalid input - Please try again")
        name = input("Enter your name: ")
    return name

main()