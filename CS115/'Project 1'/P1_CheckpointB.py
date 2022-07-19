"""
Program: CS 115 Project 1 Checkpoint B
Author: Erika Garnica Mendoza
Description: Population model for rabbits and foxes. This program asks the user for various inputs
             and later calculates the populations of rabbits and foxes. It then takes the individual
             populations of the rabbits and foxes and uses that to calculate the averages of both populations.
             It then finds the minimum population of the rabbits and the max population of the foxes.
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

    if time < 0:
        print('Error: cannot have a negative timescale')
        print(exit(-1))
    print(' ')

    # starters for average
    rabbit_popsum = 0
    fox_popsum = 0

    # min/max variable saves
    minrabbit_time = 0
    maxfox_time = 0
    rabbit_minimum = rpop
    fox_maximum = fpop

    for i in range(0, time + 1):
        original_rpop = rpop
        original_fpop = fpop

        # save min, use if statement as <
        if original_rpop < rabbit_minimum:
            rabbit_minimum = original_rpop
            minrabbit_time = i
        # save max, use if statement as >
        if original_fpop > fox_maximum:
            fox_maximum = original_fpop
            maxfox_time = i

        print('Time t = ', i, ': ', rpop, 'k', ' rabbits, ', fpop, 'k', ' foxes', sep='')
        rpop = round(rpop + (rpop * rbirths) - (rpop * rdeaths * fpop), 3)
        fpop = round(fpop + (fpop * fbirths * original_rpop) - (fpop * fdeaths), 3)
        rabbit_popsum = rabbit_popsum + original_rpop
        fox_popsum = fox_popsum + original_fpop

        # negative population if statement
        if rpop < 0:
            rpop = 0.0
        if fpop < 0:
            fpop = 0.0

    print(' ')
    print('--- Simulation Statistics ---')
    rpop_average = round(rabbit_popsum / (time + 1), 3)
    fpop_average = round(fox_popsum / (time + 1), 3)
    print("Average rabbit population: ", rpop_average, 'k', sep='')
    print('Average fox population: ', fpop_average, 'k', sep='')
    print('Min rabbit population was ', rabbit_minimum, 'k at t=', minrabbit_time, sep='')
    print('Max fox population was ', fox_maximum, 'k at t=', maxfox_time, sep='')

main()
