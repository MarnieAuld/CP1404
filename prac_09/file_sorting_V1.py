"""
CP1404 - Practical 9
File Sorting Version 1
"""

import shutil
import os


def main():
    """"""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('FilesToSort')

    file_types = ["docx", "doc", "png", "gif", "txt", "xlsx", "xls", "jpg"]     # this only works if docx runs before doc, and xlsx runs before xls

    for index, file_type in enumerate(file_types):
        type_name = file_types[index]
        os.mkdir(type_name)
        for filename in os.listdir('.'):
            if not os.path.isdir(filename):
                if type_name in filename:
                    shutil.move(filename, type_name)


main()
