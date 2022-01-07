"""
Program: CS 115 Lab 2 Part E
Author: Erika Garnica Mendoza
Description: Using the graphics package, this program will draw a square of circles.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)


    # Get the number of circles and the radius from the user.
    num_circles = int(input('How many circles? '))
    radius = int(input('Enter a number for the radius: '))

    x = radius + 10
    y = radius + 10

    # Draw the left vertical circles.
    # Copy and paste what you need from your lab02d.py here.
    for i in range(0, num_circles - 1):
        print('x =', x, 'and y =', y)
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        y = y + (radius * 2)

    # Draw the bottom horizontal circles.
    for i in range(0, num_circles - 1):
        print('x =', x, 'and y =', y)
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        x = x + (radius * 2)

    # Draw the right vertical circles.
    for i in range(0, num_circles - 1):
        print('x =', x, 'and y =', y)
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        y = y - (radius * 2)

    # Draw the top horizontal circles.
    for i in range(0, num_circles - 1):
        print('x =', x, 'and y =', y)
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        x = x - (radius * 2)
        
   # Draw the top-left-to-bottom-right diagonal circles.
    for i in range(0, num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)
        x = x + radius * 2
        y = y + (radius * 2)
        print('x =', x, 'and y =', y)

    # Draw the top-right-to-bottom-left diagonal circles.
    for i in range(0, num_circles):
        print('x =', x, 'and y =', y)
        center = Point(x , y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)
        x = x - (radius * 2)
        y = y + (radius * 2)

    window.getMouse()
    window.close()

main()
