"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_length = int(input("How long do you want the word to be: "))
number_vowels = int(input("How many vowels do you want: "))
number_consonants = int(input("How many consonants do you want: "))
choice_random = input("Arrange randomly? Y/N").upper()





word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)