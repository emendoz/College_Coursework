"""
Program: CS 115 Lab 09c
Author: Erika Garnica Mendoza
Description: This program will open a file and then search its contents
             using linear and binary search.
"""


def binary_search(search_list, value_to_find):
    """Uses a binary search function to find the position of an item in a list.

    Args:
        search_list (list): The list.
        value_to_find (str): The item to search for.

    Returns:
        int: The position of the item in the list, or None if it is not in the list.
    """
    iteration = 0
    first = 0
    last = len(search_list) - 1
    while first <= last:
        middle = (first + last) // 2
        iteration += 1
        # for i in range(1):
        # print(iteration, first, last, middle, search_list[middle])
        if value_to_find == search_list[middle]:
            print('**Binary search iterations:', iteration)
            return middle
        # if value_to_find is greater than/less than the middle it will search in the bottom or top half of the list
        elif value_to_find > search_list[middle]:
            first = middle + 1
        else:
            last = middle - 1

    print('**Binary search iterations:', iteration)
    return None

  
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

    contentList = list(fileContents)  # turns the file contents into a list
    print()
    print('The original list of cities is:')
    print_list(contentList)  # displays the contents of the original unsorted list
    print()
    print('After sorting, the new list is:')
    contentList.sort()  # sorts the list for binary search
    print_list(contentList) # displays the sorted list

    print()
    cityName = str(input('Enter the name of a city: '))

    while cityName != 'quit':
        print('The position of', cityName, 'is:')
        print('Linear search:', linear_search(contentList, cityName))
        print('Binary search:', binary_search(contentList, cityName))
        print()
        cityName = input('Enter the name of a city: ')

    # print(type(filename))    # the type is a string before split //after split list
    # print(len(filename))     # length of 507 before split //after split 68


main()
