

def main():
    word_bank = {}
    user_text = input("Text: ").lower()
    words = user_text.split()
    for word in words:
        if word in word_bank:
            word_bank[word] += 1
        else:
            word_bank[word] = 1
    for word, count in word_bank.items():
        print("{:2} : {}".format(word, count))

main()
