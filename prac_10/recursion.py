"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 0
    print(n ** 2)
    do_something(n - 1)


def do_opposite_of_something(n):
    """Print the squares of positive numbers from 0 to n or their way back after hitting base case"""
    if n >= 0:
        do_opposite_of_something(n - 1)
        print(n ** 2)


# print(do_it(5))
# do_something(4)
# do_opposite_of_something(4)
