

def main():
    word_bank = {}
#    text = input("Text: ").lower()
    text = "this is a collection of words of nice words this is a fun thing it is"
    words = text.split()
    for word in words:
        if word in word_bank:
            word_bank[word] += 1
        else:
            word_bank[word] = 1
    word_list = list(word_bank)
    word_list.sort()

    for word in word_list:
        max_word_length = max(len(word) for word in word_list)
        print("{:{}} : {}".format(word, max_word_length, word_bank[word]))

main()
