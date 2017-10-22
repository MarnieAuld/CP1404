"""
CP1404 - Practical 10
Recursion from scratch.
Write a program to get the number of rows from the user and calculate the number of blocks you will need
given the number of rows (n) to make a 2D pyramid.
Do this first as a simple loop in a function, then write a recursive function to calculate the number of
blocks. As always, think about good function design. It should take in the number of rows and return the
number of blocks.
"""


def calculate_blocks_with_loop():
    blocks = 0
    # user_rows = int(input("How many rows: "))
    user_rows = 6
    for rows in range(1, user_rows+1):
        blocks += rows
    print(blocks)


# calculate_blocks_with_loop()


def calculate_blocks_needed(rows):
    if rows <= 0:
        return 0
    return rows + calculate_blocks_needed(rows - 1)


def get_user_input():
    user_rows = int(input("How many rows: "))
    print('The number of blocks needed for {} rows is: {} blocks'.format(user_rows, calculate_blocks_needed(user_rows)))


# get_user_input()