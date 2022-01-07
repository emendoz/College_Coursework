"""
Program: CS 115 Lab 01b
Author: Erika Garnica Mendoza
Description: This program will ask you to enter a numeric value and compute the area of a square and volume of a cube,
given the lengths provided.
"""

def main():
  # Get the side length
  length = float(input("Enter a numeric value: "))
  
  # Compute the area of the square
  square_area = length * length
  # Compute the volume of the cube
  cube_volume = length * length * length
  
  print("The area of a square with side length ", length, " is ", square_area, '.', sep="")
  
  print("The volume of a cube with edge length ", length, " is ", cube_volume, '.', sep="")
  
 main()
