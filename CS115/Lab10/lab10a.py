"""
Program: CS 115 Lab 10a
Author: Erika Garnica Mendoza
Description: Asks the user for a file name and prints it as a nice list.
             It then finds the index of the min within the lists provided by print statements.
"""


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


def find_index_of_min(L):
    """Returns the index of the minimum element of L. (We assume L contains
    no duplicate elements, for simplicity).

    Args:
        L (list): A list of strings.

    Returns:
        int: The index of the minimum element of L.
    """
    accumulator = 0

    # to calculate the min of an empty list
    if len(L) == accumulator:
        return None
    # to find the index of the min in a list
    elif len(L) - 1 == accumulator:
        return accumulator  # save our value for later
    minimum = accumulator   # minimum is different every time accumulator cycles through
    for i in range(minimum + 1, len(L)):    # checks every item in the list to find the minimum
        if L[i] < L[minimum]:
            minimum = i
    return minimum


def main():
    """Asks user for file name and prints it as a list.
    Prints output of the statements provided.
    """
    namefile = input("Name of input file: ")

    print()
    fileContents = readfile(namefile)

    print("The original list of cities is: ")
    print_list(fileContents)

    # Part A print statements
    print(find_index_of_min([]))
    print(find_index_of_min([3, 2, 1, 0]))
    print(find_index_of_min(['A', 'Z', 'Y', 'B']))
    print(find_index_of_min(['B', 'A', 'Z', 'Y']))


main()
