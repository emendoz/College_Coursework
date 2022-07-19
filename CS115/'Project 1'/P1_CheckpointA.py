"""
Program: CS 115 Project 1 Checkpoint A
Author: Erika Garnica Mendoza
Description: Population model for rabbits and foxes. This program asks the user for various inputs
             and later calculates the populations of rabbits and foxes.
"""


def main():
    print('==> Rabbits and Foxes Population Simulation <==')
    print(' ')
    print('--- Model Parameters ---')

    rbirths = float(input('Rabbits birth rate: '))
    rdeaths = float(input('Rabbits death rate: '))
    fbirths = float(input('Foxes birth rate: '))
    fdeaths = float(input('Foxes death rate: '))
    print(' ')

    print('--- Initial Population ---')
    rpop = float(input('Number of rabbits (in thousands) at t = 0: '))
    fpop = float(input('Number of foxes (in thousands) at t = 0: '))
    time = int(input('Timescale: '))
    print(' ')

    for i in range(0, time + 1):
        originalrpop = rpop
        print('Time t = ', i, ': ', rpop, 'k', ' rabbits, ', fpop, 'k', ' foxes', sep='')
        rpop = round(rpop + (rpop * rbirths) - (rpop * rdeaths * fpop), 3)
        fpop = round(fpop + (fpop * fbirths * originalrpop) - (fpop * fdeaths), 3)

main()
