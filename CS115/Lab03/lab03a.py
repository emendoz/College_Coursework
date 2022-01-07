"""
Program: CS 115 Lab 3a
Author: Erika Garnica Mendoza
Description: This program uses the graphics package
to interact with the user.
"""
from graphics import *


def main():
    window = GraphWin('Lab 3a_1', 400, 600)

    for i in range(5):
        click_point = window.getMouse()
        click_point_x = click_point.getX()
        click_point_y = click_point.getY()
        print('x = ', click_point_x, ', y = ', click_point_y, sep="")
        pt = window.getMouse()  # get a click
        c = Circle(pt, 20)  # draw a circle centered there
        c.draw(window)


    window.getMouse()
    window.close()

main()
