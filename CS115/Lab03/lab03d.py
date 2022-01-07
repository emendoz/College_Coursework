"""
Program: CS 115 Lab 3d
Author: Erika Garnica Mendoza
Description: This program prompts the user for the number of rows and the number of columns.
It then draws a grid of rectangles and fills them randomly. When clicked on, it also shows the x and y-coordinate clicks
as well as the row and column it is in.
"""
from graphics import *
from random import seed, randint


def random_color():
    """Produces a random color.

    Returns:
        str: a string representing a color.
    """
    # Note: Don't worry about the details of this function right now.
    colors = ['blue', 'blue2', 'blue3', 'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3', 'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3', 'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3', 'pink', 'pink1', 'pink2', 'pink3']
    return colors[randint(0, len(colors) - 1)]


def main():
    seed()  # Initialize random number generator
    window = GraphWin('Lab 3d', 800, 800)

    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 60

    num_rows = int(input('Number of rows: '))
    num_columns = int(input('Number of columns: '))

    for r in range(num_rows):
        y = top_left_y + num_rows * height
        top_left_y = top_left_y + width

        for i in range(num_columns):
            x = top_left_x + num_columns * width
            top_left_x = top_left_x + width
            top_left_point = Point(top_left_x, top_left_y)
            bottom_right_point = Point(top_left_x + width, top_left_y + height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
            enclosing_rectangle.setFill(random_color())
            enclosing_rectangle.draw(window)
        top_left_x = 100

    row = 0
    column = 0
    for i in range(0, 10):
        c_point = window.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
        row = (c_point.getY() - top_left_y) / height
        column = (c_point.getX() - top_left_x) / width
        if (top_left_x.getX() <= x_c_point <= bottom_right_point.getX() and
           top_left_y.getY() <= y_c_point <= bottom_right_point.getY()):
            print('The click at ', (int(c_point.getX()), int(c_point.getY())), ' is in row ', int(row), ' column ',
                  int(column), '.', sep='')
        else:
            print('The click at', (int(c_point.getX()), int(c_point.getY())), 'is outside of the grid.', sep='')

    window.getMouse()
    window.close()
    
main()
