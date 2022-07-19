"""
Program: CS 115 Lab 10c
Author: Erika Garnica Mendoza
Description: Asks the user for a file name and prints it as a nice list.
             It then sorts the list while showing what elements within the list were swapped.
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


def find_index_of_min(L, start_index):
    """Returns the index of the minimum element of L. (We assume L contains
    no duplicate elements, for simplicity).

    Args:
        L (list): A list of strings.
        start_index (int): A integer within a list.

    Returns:
        int: The index of the minimum element of L.
    """

    # to calculate the min of a list if it contains the starting index
    if len(L) <= start_index:
        return None
    # to find the index of the min in a list
    elif len(L) - 1 == start_index:
        return start_index  # save our value for later
    minimum = start_index
    for i in range(minimum + 1, len(L)):  # checks every item in the list to find the minimum
        if L[i] < L[minimum]:
            minimum = i
    return minimum


def selection_sort(L):
    """Uses the selection sort algorithm to sort a list.
    Sorts the original list that was passed to it (has no return value).

    Args:
        L (list): The unsorted list.
    """

    for i in range(len(L) - 1):
        min_indx = find_index_of_min(L, i)
        # prints elements that were swapped
        print('Swapped elements', i, 'and', min_indx, '--', L[i], 'and', L[min_indx])
        # Swap the found minimum element with the first element
        L[i], L[min_indx] = L[min_indx], L[i]


def main():
    """Asks user for file name and prints it as a list.
    Takes list and prints out a sorted version of it.
    """
    namefile = input("Name of input file: ")

    print()
    fileContents = readfile(namefile)

    print("The original list of cities is: ")
    print_list(fileContents)
    selection_sort(fileContents)

    print()
    print("The new list of cities is: ")
    print_list(fileContents)


main()
