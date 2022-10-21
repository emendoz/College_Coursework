"""
Program: CS454 Project1 Problem 2
Author: Erika Mendoza
Description: This file Problem2.py contains a function called FindString(). 
This function returns the shortest string accepted by DFA M.
"""

def FindString():
    """
    :input params: k = positive int greater than one, digits = input alphabet
    :return: N = shortest string accepted by DFA M
    """
    k = int(input('Enter a positive integer:\n'))
    digits = [int(i) for i in 
    input('Enter subset of digits permitted\n(Accepts input with commas or spaces (#, # or # # #)):\n').replace(',', ' ').split()]

    D = [float("inf")] * k
    parent = [(-1, 0)] * k

    # Initialize a queue Q
    Q = []
    for i in digits:
        if ( i != 0 ):
            if (D[i % k] > 10 ** 9):
                Q.append(i % k)
                D[i % k] = 1
                parent[i % k] = -1, i

    while( len(Q) > 0 ):
        curr = Q.pop(0)
        for i in digits:
            next_ = (curr * 10 + i) % k
            if ( D[curr] + 1 < D[next_] ):
                D[next_] = D[curr] + 1
                Q.append(next_)
                parent[next_] = curr, i

    if ( D[0] > 10 ** 9 ):
        output = "No solution."
        return output
    else:
        N = ""
        curr = 0
        while ( curr != -1 ):
            N += str(parent[curr][1])
            curr = parent[curr][0]
        N = N[::-1] # reverse string
    
    # output the resulting string
    return N

def main():

    print(FindString())
    
main()