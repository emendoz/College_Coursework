"""
Program: CS 115 Lab 2 Part D
Author: Erika Garnica Mendoza
Description: Using the graphics package, this program will draw a number of circles using a for-loop.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    x = 100
    y = 100

    radius = int(input('Enter a number for the radius: '))
    num_circles = int(input('How many circles? '))

    for i in range(num_circles):
        print('x =', x, 'and y =', y)
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)
        y = y + (radius * 2)

    window.getMouse()
    window.close()


main()

