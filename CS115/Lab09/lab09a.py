"""
Program: CS 115 Lab 09a
Author: Erika Garnica Mendoza
Description: This program will open a file and then search its contents
             using linear and binary search.
"""

def print_list(list_to_print):
    """Prints the contents of a list.

    Args:
        list_to_print (list): The list to print.
    """
    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")

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


def main():
    """Reads and prints a file's contents.
    """

    filename = str(input("Name of input file: "))

    fileContents = readfile(filename)  # retrieves the contents of the file

    print('Number of lines in file:', len(fileContents))

    print_list(list(fileContents))
    # print(type(filename))    # the type is a string before split //after split list
    # print(len(filename))     # length of 507 before split //after split 68

main()
