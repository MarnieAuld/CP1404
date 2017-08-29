
user_text = input("Text: ")
words = user_text.split()
word_bank = []

for word in words:
    if word in word_bank:
        word_bank[word] += 1
    else:
        word_bank[word] = 1

counted_words = word_bank.items()

print("{} ").format(word)