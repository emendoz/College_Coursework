"""
Program: CS 115 Project 1
Author: Erika Garnica Mendoza
Description: Population model for rabbits and foxes. This program asks the user for various inputs
             and later calculates the populations of rabbits and foxes in tune with the change of time.
             It then takes the individual populations of the rabbits and foxes and uses that to 
             calculate the averages of both populations as well as the minimum of the rabbit population
             and maximum of the fox population.
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
    # If input is below zero, populations are negated.
    if rpop < 0:
        rpop = 0.0
    if fpop < 0:
        fpop = 0.0
    # If time is below zero, then no population growth is occurring.
    if time < 0:
        print('Error: cannot have a negative timescale')
        print(exit(-1))
    print(' ')

    # Population sum variables set to zero to be able to add changing populations to it later on.
    rabbit_pop_sum = 0
    fox_pop_sum = 0

    # minimum and maximum time variables
    min_rabbit_time = 0
    max_fox_time = 0
    # min/max variables save initial population changes
    rabbit_minimum = rpop
    fox_maximum = fpop

    for i in range(0, time + 1):
        original_rpop = rpop
        original_fpop = fpop

        # saved min, use if statement as < to get min and time to be in the same range
        if original_rpop < rabbit_minimum:
            rabbit_minimum = original_rpop
            min_rabbit_time = i
        # saved max, use if statement as > to get max and time to be in the same range
        if original_fpop > fox_maximum:
            fox_maximum = original_fpop
            max_fox_time = i

        print('Time t = ', i, ': ', rpop, 'k', ' rabbits, ', fpop, 'k', ' foxes', sep='')
        rpop = round(rpop + (rpop * rbirths) - (rpop * rdeaths * fpop), 3)
        fpop = round(fpop + (fpop * fbirths * original_rpop) - (fpop * fdeaths), 3)
        rabbit_pop_sum = rabbit_pop_sum + original_rpop
        fox_pop_sum = fox_pop_sum + original_fpop

    print(' ')
    print('--- Simulation Statistics ---')
    # equations to calculate averages
    rpop_average = round(rabbit_pop_sum / (time + 1), 3)
    fpop_average = round(fox_pop_sum / (time + 1), 3)
    print("Average rabbit population: ", rpop_average, 'k', sep='')
    print('Average fox population: ', fpop_average, 'k', sep='')
    print('Min rabbit population was ', rabbit_minimum, 'k at t=', min_rabbit_time, sep='')
    print('Max fox population was ', fox_maximum, 'k at t=', max_fox_time, sep='')

main()
