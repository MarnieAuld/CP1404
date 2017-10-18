"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics')

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    # for filename in os.listdir('.'):
    #     # ignore directories, just process files
    #     if not os.path.isdir(filename):
    #         new_name = get_fixed_filename(filename)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory

    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)
        for file in file_list:
            new_name = get_fixed_filename(file)
            # os.rename(source_path, destination_path)
            os.rename(os.path.join(dir_name, file), os.path.join(dir_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename.
    Loop through filenames for names without "_"
    |   Loop through characters in filename and insert "_" between islower() and isupper()
    Loop through characters in filename and replace character.isupper() after "_"
    """
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    if "_" not in filename:
        characters = list(filename)
        for index, character in enumerate(characters):
            if character.isupper() and characters[index-1].isalpha() and index > 0:
                characters.insert(index, "_")
        filename = "".join(characters)
    else:
        characters = list(filename)
        for index, character in enumerate(characters):
            if character == "_":
                characters[index+1] = characters[index+1].upper()
        filename = "".join(characters)
    new_name = filename
    return new_name


main()
