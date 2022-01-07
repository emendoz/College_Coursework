"""
Program: CS 115 Lab 01a
Author: Erika Garnica Mendoza
Description: This program will ask you to enter a numeric value and compute the area of a square, given the side length.
"""

def main():
  # Get the side length
  length = float(input("Enter a numeric value: "))
  
  # Compute the area of the square
  square_area = length * length
  
  print("The area of a square with side length ", length, " is ", square_area, '.', sep="")
  
 main()
