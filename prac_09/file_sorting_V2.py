"""
CP1404 - Practical 9
File Sorting Version 2
"""

import shutil
import os


def main():
    """"""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('FilesToSort(1)')

    # file_types = ["docx", "doc", "png", "gif", "txt", "xlsx", "xls", "jpg"]
    file_types = []
    for filename in os.listdir('.'):
        file_extension = os.path.splitext(filename)[1]
        if file_extension not in file_types:
            file_types.append(file_extension)

    # make new directories
    # os.mkdir('Spreadsheets')
    # os.mkdir('Images')
    # os.mkdir('Docs')

    for file_type in file_types:
        chosen_folder = input("What category would you like to sort {} files into? ".format(file_type))
        if not os.path.exists(chosen_folder):
            os.mkdir(chosen_folder)
        for filename in os.listdir('.'):
            if not os.path.isdir(filename):
                if file_type in filename:
                    shutil.move(filename, chosen_folder)


main()
