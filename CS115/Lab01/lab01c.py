"""
Program: CS 115 Lab 01c
Author: Erika Garnica Mendoza
Description: This program will ask you to enter a
numeric value and compute the following(while also rounding): 
area of a square, volume of a cube, and the volume of a sphere, given the lengths provided.
"""

import math

def main():
    # Get the side length
    length = float(input('Enter a numeric value: '))

    # Compute the area of the square
    square_area = length * length
    # Compute the volume of the cube
    cube_volume = length * length * length
    # Compute the volume of the sphere
    sphere_volume = 4 / 3 * math.pi * cube_volume

    print("The area of a square with side length ", length,
          " is ", round(square_area, 3), ".", sep="")

    print("The volume of a cube with edge length ", length,
          " is ", round(cube_volume, 3), ".", sep="")

    print("The volume of a sphere with radius length ", length,
          " is ", round(sphere_volume, 3),  ".", sep="")


main()
