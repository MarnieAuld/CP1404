"""
CP1404 - Practical q0
Wikipedia API & Python Library
"""

import wikipedia


def main():
    search_input = input("Enter page title or search phrase: ").capitalize()
    while search_input:
        wiki_page = search(search_input)
        wiki_page_details = wikipedia.page(wiki_page)
        print("Wiki Title: {} \nSummary: {} \nURL: {}"
              .format(wiki_page_details.title, wiki_page_details.summary, wiki_page_details.url))
        print()
        search_input = input("Enter page title or search phrase: ").capitalize()


def search(phrase):
    try:
        wikipedia.summary(phrase)
        return phrase
    except wikipedia.DisambiguationError:
        print("That search phrase may refer to: ")
        wiki_pages = wikipedia.search(phrase)
        for index, wiki_page in enumerate(wiki_pages):
            print("{} - {} \n".format(index, wiki_page))
        wiki_page_number = int(input("What number page title: "))
        return wiki_pages[wiki_page_number]

main()
