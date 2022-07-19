"""
Program: CS 115 Lab 09b
Author: Erika Garnica Mendoza
Description: This program will open a file and then search its contents
             using linear and binary search.
"""


def linear_search(search_list, value_to_find):
    """Uses linear search to find the position of an item in a list.

    Parameters:
        search_list (list): The list.
        value_to_find (str): The item to search for.

    Returns:
        int: The position of the item in the list, or None if not found.
    """
    for i in range(len(search_list)):
        if search_list[i] == value_to_find:
            return i

def readfile(filename):
    """Reads the entire contents of a file into a single string using
    the read() method.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The text in the file as a large, possibly multi-line, string.
    """
    infile = open(filename, 'r')  # opens file for reading

    filetext = infile.read().splitlines()  # reads the file contents into filetext

    infile.close()  # closes the file

    return filetext  # returns text of the file, as a long string


def print_list(list_to_print):
    """Prints the contents of a list.

    Args:
        list_to_print (list): The list to print.
    """
    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")

def main():
    """Reads and prints a file's contents.
    """

    filename = str(input('Name of input file: '))

    fileContents = readfile(filename)  # retrieves the contents of the file and saves as str

    # print('Number of lines in file:', len(fileContents))

    contentList = list(fileContents)   # turns the file contents into a list
    print_list(contentList)    # displays the contents of list accordingly

    print()
    cityName = str(input('Enter the name of a city: '))

    while cityName != 'quit':
        position = linear_search(contentList, cityName)
        print('The position of', cityName, 'is:')
        print('Linear search:', position)

        print()
        cityName = input('Enter the name of a city: ')

    # print(type(filename))    # the type is a string before split //after split list
    # print(len(filename))     # length of 507 before split //after split 68

main()
