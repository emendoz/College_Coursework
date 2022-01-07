"""
Program: CS 115 Lab 8b
Author: Erika Garnica Mendoza
Description: This program will create a magic square
whose size is specified by the user, it then declares whether
it is a magic square or not and proceeds to ask the user for filename.
Then it accesses that filename's matrix of numbers and declares if it's a
magic square as well.
"""
import sys


def build_magic_square(square):
    """Modifies 'square' to fill it with a magic square. Modifies
    the original list (has no return value).

    Args:
        square (list): a 2D array whose number of rows and columns
                are equal and len(square) is an odd number.
    """
    magic_value = 1
    square_size = len(square)
    row = 0
    col = square_size // 2
    square_size_squared = square_size * square_size
    while magic_value <= square_size_squared:
        square[row][col] = magic_value
        row -= 1
        col += 1
        if row < 0 and col > square_size - 1:
            row += 2
            col -= 1
        elif row < 0:
            row = square_size - 1
        elif col > square_size - 1:
            col = 0
        elif square[row][col] != 0:
            row += 2
            col -= 1

        magic_value += 1

def sum_row_values(matrix, row_number):
    """Sums the values of all entries in the row given by 'row_number'.

    Args:
        matrix (list): A square, 2D array.
        row_number (int): A value in the range 0 and len(matrix)-1.

    Returns
        int: The sum of all values of the row indicated by 'row_number'.
    """

    row_total = matrix[row_number]
    return sum(row_total)

  
def sum_col_values(matrix, col_number):
    """Sums the values of all entries in the column given by 'col_number'.

    Args:
        matrix (list): A 2D, square array.
        col_number (int): A value in the range 0 and len(matrix)-1.

    Returns:
        int: The sum of all values in the column indicated by 'col_number'.
    """

    col_total = matrix[col_number]
    return sum(col_total)


def sum_top_left_bottom_right_diagonal(matrix):
    """Calculates the sum of the values at matrix[0][0],
    matrix[1][1], etc.

    Args:
        matrix (list): A square, 2D array.

    Returns:
        int: The sum of values of the top-left to bottom-right diagonal.
    """

    total = []
    for i in range(len(matrix)):
        num = matrix[i][i]
        total.append(num)
    return sum(total)


def sum_top_right_bottom_left_diagonal(matrix):
    """Calculates the sum of the values at matrix[0][len(matrix)-1],
    matrix[1][len(matrix)-2], etc.

    Args:
        matrix (list): A square, 2D array.

    Returns:
        int: The sum of values of the top-right to bottom-left diagonal
    """

    total = []
    for i in range(len(matrix)):
        num = matrix[i][len(matrix) - 1 - i]
        total.append(num)
    return sum(total)

  
def is_magic_square(matrix):
    """Returns True if the two dimensional array 'matrix' is a magic square;
    otherwise, returns False.

    Args:
        matrix (list): A square, 2D array.

    Returns:
        bool: True or False.
    """

    # Calculate the sum of the values of the top-left to
    #   bottom-right diagonal. Call it tlbr_sum.
    tlbr_sum = sum_top_left_bottom_right_diagonal(matrix)

    # Calculate the sum of the values of the top-right to
    #   bottom-left diagonal. Call it trbl_sum.
    trbl_sum = sum_top_right_bottom_left_diagonal(matrix)

    # If tlbr_sum is not equal to trbl_sum, return False.
    # Otherwise, proceed.
    if tlbr_sum != trbl_sum:
        print('The above square is NOT a magic square.')
        return False

    # Calculate the sum of each row of the matrix and compare it
    #  with tlbr_sum. If the two sums are not equal, return False.
    #  Otherwise, proceed.
    for row_number in range(len(matrix)):
        sum_of_rows = sum_row_values(matrix, row_number)
        if sum_of_rows != tlbr_sum:
            print('The above square is NOT a magic square.')
            return False

    # Calculate the sum of each column of the matrix and compare it
    #  with tlbr_sum. If the two sums are not equal, return False.
    #  Otherwise, proceed.
    for col_number in range(len(matrix)):
        sum_of_cols = sum_col_values(matrix, col_number)
        if sum_of_cols != tlbr_sum:
            print('The above square is NOT a magic square.')
            return False

    # return True.
    else:
        print('The above square is a magic square.')
        return True


def read_magic_square(filename):
    """Reads values from a file into a 2D list.

    Args:
        filename (str): The name of the file.

    Returns:
        list: A 2D list of integer values.
    """

    infile = open(filename, 'rt')
    square = []  # start with an empty list

    for line in infile:  # read text from file
        row = []
        numbers = line.split()

        # Loop through the list of numbers.
        # Append each number to the row.
        for num in numbers:
            row.append(int(num))

        if len(row) > 0:  # Don't count blank lines
            square.append(row)  # Append the row to the 2D list

    return square


def create_list(rows, cols):
    """Creates a two-dimensional array.

    Args:
        rows (int): The numbers of rows.
        cols (int): The number of columns.

    Returns:
        list: A 2D array with all values set to zero.
    """
    two_d = []  # create an empty list
    for i in range(rows):
        two_d.append([])  # append an empty list to two_d
        for j in range(cols):
            two_d[i].append(0)  # two_d[i] is the empty list that we just created.
            # here, we are adding elements to it.
    return two_d


def rjust_by_n(number, n):
    """Formats a string containing 'number', right-justified.

    Args:
        number (int): A value.
        n (int): The width of the string into which 'number' is inserted.

    Returns:
        str: A string of length n.
    """

    return str(number).rjust(n)


def print_list(numbers):
    """Prints a 1D list of numbers, where each number is right-justified.

    Args:
        numbers (list): A list of numbers.
    """
    for i in range(len(numbers)):
        print(rjust_by_n(numbers[i], 4), end='')
    print()


def print_2d_list(two_d_list):
    """Prints a 2-dimensional list in a pretty format.

    Args:
        two_d_list (list): A 2D list of numbers.
    """
    for i in range(len(two_d_list)):
        print_list(two_d_list[i])

    return two_d_list


def main():
    square_size = int(input('Enter an odd integer to build a magic square: '))

    if square_size % 2 == 1:
        # creates the matrix
        print()
        square_size = create_list(square_size, square_size)
        build_magic_square(square_size)
        print_2d_list(square_size)

        # evaluates it if it is a magic square
        print()
        is_magic_square(square_size)

        print()
        file_name = input("Enter the name of a file containing a matrix of numbers: ")

        print()
        file_magic_square = read_magic_square(file_name)
        create_list(len(file_magic_square), len(file_magic_square))
        print_2d_list(file_magic_square)

        print()
        is_magic_square(file_magic_square)
    else:
        sys.exit(print(square_size, 'is not an odd integer. Terminating. . .'))


main()
  
