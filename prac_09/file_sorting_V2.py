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

    file_types = ["docx", "doc", "png", "gif", "txt", "xlsx", "xls", "jpg"]

    # make new directories
    os.mkdir('Spreadsheets')
    os.mkdir('Images')
    os.mkdir('Docs')

    for file_type in file_types:
        chosen_folder = input("What category would you like to sort {} files into? ".format(file_type))
        for filename in os.listdir('.'):
            if not os.path.isdir(filename):
                pass
