"""
Program: CS 115 Lab02b
Author: Erika Garnica Mendoza
Description: Using the graphics package, this program will draw five circles.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)
    
    # create a circle centered at (100, 200) with radius 40
    circle = Circle(Point(100, 200), 40) 
    circle.setOutline('blue')
    # draw the circle in the window that we created earlier
    circle.draw(window) 

    # create a circle centered at (75, 45) with radius 55
    circle = Circle(Point(75, 45), 55)  
    circle.setOutline('violet red')
    # draw the circle in the window that we created earlier
    circle.draw(window)
    
    # create a circle centered at (500, 300) with radius 100
    circle = Circle(Point(500, 300), 100)  
    circle.setOutline('SpringGreen4')
    # draw the circle in the window that we created earlier
    circle.draw(window)

    # create a circle centered at (200, 600) with radius 30
    circle = Circle(Point(200, 600), 30)
    circle.setOutline('gray5')
    # draw the circle in the window that we created earlier
    circle.draw(window)

    # create a circle centered at (750, 500) with radius 200
    circle = Circle(Point(750, 500), 200)
    circle.setOutline('olive drab')
    # draw the circle in the window that we created earlier
    circle.draw(window)

    window.getMouse()                # wait for the mouse to be clicked in the window
    window.close()                   # close the window after the mouse is clicked in the window


main()
