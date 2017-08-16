
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

MENU = """E - Even Numbers
O - Odd Numbers
S - Square Numbers
Q - Quit Program"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        if x % 2 == 0 and y % 2 == 0:
            for i in range(x, y + 1, 2):
                print(i, end=' ')
                print()
        elif x % 2 == 0 and y % 2 == 1:
            for i in range(x, y, 2):
                print(i, end=' ')
                print()
        elif x % 2 == 1 and y % 2 == 0:
            for i in range(x + 1, y + 1, 2):
                print(i, end=' ')
                print()
        else:
            for i in range(x + 1, y + 1, 2):
                print(i, end=' ')
                print()

    elif choice == "O":
        if x % 2 == 0 and y % 2 == 0:
            for i in range(x + 1, y, 2):
                print(i, end=' ')
                print()
        elif x % 2 == 0 and y % 2 == 1:
            for i in range(x + 1, y + 1, 2):
                print(i, end=' ')
                print()
        elif x % 2 == 1 and y % 2 == 0:
            for i in range(x, y, 2):
                print(i, end=' ')
                print()
        else:
            for i in range(x, y + 1, 2):
                print(i, end=' ')
                print()

    elif choice == "S":
        for i in range(x, y, 1):
            square = i * i
            print(i,"*", i, "=", square, end=' ')
            print()

    else:
        print("Invalid option - Please Select Again")
        print(MENU)
        choice = input(">>> ")

print("Thank you.")