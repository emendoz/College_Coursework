"""
Program: CS 115 Lab 7c
Author: Erika Garnica Mendoza
Description: This program computes geometric quantities.
"""
import sys
import math


def get_numeric_val():
    """Prompts the user for a number. Exits if the user does not
    enter a positive value; otherwise, returns the value they entered.

    Returns:
        float: The number entered by the user.
    """
    num = float(input('Enter a positive numeric value: '))
    if num <= 0:
        sys.exit('Error: that number was not positive.')
    return num


def get_menu_choice():
    """Prints a menu and returns the user's selection.

    Returns:
        str: A single character ('q', 'a', 'b', 'c', etc).
    """

    print("Would you like to")
    print("a. Calculate the area of a square?")
    print("b. Calculate the area of a circle?")
    print("c. Calculate the volume of a cube?")
    print("d. Calculate the volume of a sphere?")
    print("e. Calculate the area of an equilateral triangle?")
    print("q. Quit?")

    user_input = input("").lower()
    return user_input


def compute_square_area(side):
    """Computes the area of a square.

    Args:
        side (float): The side length for the square.

    Returns:
        float: The area.
    """

    square_area = float(side * side)
    return square_area


def compute_circle_area(radius):
    """Computes the area of a circle.

    Args:
        radius (float): The radius length for the circle.

    Returns:
        float: The area.
    """

    circle_area = float(math.pi * (radius ** 2))
    return circle_area
  
def compute_cube_volume(edge):
    """Computes the volume of a cube.

    Args:
        edge (float): The side length for the cube.

    Returns:
        float: The volume.
    """

    cube_volume = (edge ** 3)
    return cube_volume


def compute_sphere_volume(radius):
    """Computes the volume of a sphere.

    Args:
        radius (float): The radius length for a sphere.

    Returns:
        float: The volume.
    """

    sphere_volume = float((4 / 3) * math.pi * (radius ** 3))
    return sphere_volume


def compute_tri_area(side):
    """Computes the area of an equilateral triangle.

    Args:
        side (float): The side length for a triangle.

    Returns:
        float: The volume.
    """

    equilateral_triangle_area = float((side ** 2) * (math.sqrt(3) / 4))
    return equilateral_triangle_area

def main():
    menu_choice = get_menu_choice()  # Get the user's first choice

    while menu_choice != 'q':
        user_num = get_numeric_val()  # Get the side length (etc.)

        if menu_choice == 'a':
            print('The area of a square with side length ', user_num,
                  ' is ', round(compute_square_area(user_num), 5), '.', sep="")
        elif menu_choice == 'b':
            print('The area of a circle with radius length ', user_num,
                  ' is ', round(compute_circle_area(user_num), 5), '.', sep="")
        elif menu_choice == 'c':
            print('The volume of a cube with edge length ', user_num,
                  ' is ', round(compute_cube_volume(user_num), 5), '.', sep="")
        elif menu_choice == 'd':
            print('The volume of a sphere with radius length ', user_num,
                  ' is ', round(compute_sphere_volume(user_num), 5), '.', sep="")
        elif menu_choice == 'e':
            print('The volume of an equilateral triangle with radius length ', user_num,
                  ' is ', round(compute_tri_area(user_num), 5), '.', sep="")

        menu_choice = get_menu_choice()  # Get user's next choice


main()
