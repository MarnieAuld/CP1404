out_file = open("name_file.txt", 'w')
name = input("Please enter your name: ")
out_file.write(name)
out_file.close()

in_file = open("name_file.txt", 'r')
name = in_file.read()
print("Your name is: ", name)
in_file.close()

in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)
in_file.close()