"""
Program: CS 115 Lab02a
Author: Erika Garnica Mendoza
Description: This program adds up the numbers from 1 to 5.
"""

def main():
    total = 0

    for i in range(1, 6):
        i = float(input('Enter an integer: '))
        total = total + i

    print('The total is:', round(total))

    print('The mean is:', total / 5)

main()
