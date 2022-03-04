"""
hw5.py
Name(s): William "Cason" Pierce
NetId(s): wcp17
Date: 2-26-22
"""

import math
import numpy
import matplotlib.pyplot as plt

"""
This is the function f(x) to be integrated.
"""

def f(x):
    return math.cos(x / 10)


"""
Left Point Rule: This function computes the Left Hand Riemann Sum of f(x) (defined above) 
using the specified input parameters.

INPUTS:
N: the number of subintervals used to compute the Riemann Sum
a: the lower bound of integration
b: the upper bound of integration

OUTPUTS:
integralLeft: the approximate value of the intergral of f(x) from a to b 
using a Left Hand Riemann Sum of N subintervals
"""

def left(N, a, b):
    # Assign deltaX to the length of a subinterval
    deltaX = (b - a) / N

    # Add the y value for each left hand endpoint to total
    total = 0
    for i in range(N):
        xVal = a + (deltaX * i)
        yVal = f(xVal)
        total += yVal

    # Multiply total by the length for each subinterval
    integralLeft = deltaX * total

    return integralLeft


"""
Right Point Rule: This function computes the Right Hand Riemann Sum of f(x) (defined above) 
using the specified input parameters.

INPUTS:
N: the number of subintervals used to compute the Riemann Sum
a: the lower bound of integration
b: the upper bound of integration

OUTPUTS:
integralRight: the approximate value of the intergral of f(x) from a to b 
using a Right Hand Riemann Sum of N subintervals
"""

def right(N, a, b):

    # Assign deltaX to the length of a subinterval
    deltaX = (b - a) / N

    # Add the y value for each right hand endpoint to total
    total = 0
    for i in range(1, N + 1):
        xVal = a + (deltaX * i)
        yVal = f(xVal)
        total += yVal

    # Multiply total by the length for each subinterval
    integralRight = deltaX * total

    return integralRight


"""
Trapezoidal Rule: This function computes the Riemann Sum of f(x) (defined above) using 
the trapezoidal rule and the specified input parameters

INPUTS:
N: the number of subintervals used to compute the Riemann Sum
a: the lower bound of integration
b: the upper bound of integration

OUTPUTS:
integralTrap: the approximate value of the intergral of f(x) from a to b 
using a Riemann Sum with the Trapezoidal rule of N subintervals
"""


def trap(N, a, b):
    deltaX = (b - a) / N

    sumTrap = 0
    for i in range(1, N):
        xVal = a + (deltaX * i)
        yVal = f(xVal)
        sumTrap += yVal

    integralTrap = (deltaX / 2.0) * (f(a) + f(b) + 2 * sumTrap)

    return integralTrap


"""
main
"""
if __name__ == '__main__':
    # Set the values of a and b.
    a = 0
    b = 1 / 2

    # Set the correct solution to compare against.
    correct = 10 * math.sin(1 / 20)

    # Create empty arrays lists for the left, right, and trapezoid
    # absolute errors
    leftErr = [0.0 for i in range(0, 12)]
    rightErr = [0.0 for i in range(0, 12)]
    trapErr = [0.0 for i in range(0, 12)]

    # The following code will test different values of N to compute the integral approximations using
    # each of the three functions defined above and assign their errors
    # to the proper list for plotting

    # N = 100:
    left100 = left(100, a, b)
    right100 = right(100, a, b)
    trap100 = trap(100, a, b)
    print("N = 100:")
    print("Left:", left100)
    print("Right:", right100)
    print("Trapezoid:" , trap100)
    leftErr[0] = abs(correct - left100)
    rightErr[0] = abs(correct - right100)
    trapErr[0] = abs(correct - trap100)

    # N = 500:
    left500 = left(500, a, b)
    right500 = right(500, a, b)
    trap500 = trap(500, a, b)
    print("N = 500:")
    print("Left:", left500)
    print("Right:", right500)
    print("Trapezoid:", trap500)
    leftErr[1] = abs(correct - left500)
    rightErr[1] = abs(correct - right500)
    trapErr[1] = abs(correct - trap500)

    # N = 1000:
    left1000 = left(1000, a, b)
    right1000 = right(1000, a, b)
    trap1000 = trap(1000, a, b)
    print("N = 1000:")
    print("Left:", left1000)
    print("Right:", right1000)
    print("Trapezoid:", trap1000)
    leftErr[2] = abs(correct - left1000)
    rightErr[2] = abs(correct - right1000)
    trapErr[2] = abs(correct - trap1000)

    # N = 5000:
    left5000 = left(5000, a, b)
    right5000 = right(5000, a, b)
    trap5000 = trap(5000, a, b)
    print("N = 5000:")
    print("Left:", left5000)
    print("Right:", right5000)
    print("Trapezoid:", trap5000)
    leftErr[3] = abs(correct - left5000)
    rightErr[3] = abs(correct - right5000)
    trapErr[3] = abs(correct - trap5000)

    # N = 10000:
    left10000 = left(10000, a, b)
    right10000 = right(10000, a, b)
    trap10000 = trap(10000, a, b)
    print("N = 10000:")
    print("Left:", left10000)
    print("Right:", right10000)
    print("Trapezoid:", trap10000)
    leftErr[4] = abs(correct - left10000)
    rightErr[4] = abs(correct - right10000)
    trapErr[4] = abs(correct - trap10000)

    # N = 50000:
    left50000 = left(50000, a, b)
    right50000 = right(50000, a, b)
    trap50000 = trap(50000, a, b)
    print("N = 50000:")
    print("Left:", left50000)
    print("Right:", right50000)
    print("Trapezoid:", trap50000)
    leftErr[5] = abs(correct - left50000)
    rightErr[5] = abs(correct - right50000)
    trapErr[5] = abs(correct - trap50000)

    # N = 100000:
    left100000 = left(100000, a, b)
    right100000 = right(100000, a, b)
    trap100000 = trap(100000, a, b)
    print("N = 100000:")
    print("Left:", left100000)
    print("Right:", right100000)
    print("Trapezoid:", trap100000)
    leftErr[6] = abs(correct - left100000)
    rightErr[6] = abs(correct - right100000)
    trapErr[6] = abs(correct - trap100000)

    # N = 500000:
    left500000 = left(500000, a, b)
    right500000 = right(500000, a, b)
    trap500000 = trap(500000, a, b)
    print("N = 500000:")
    print("Left:", left500000)
    print("Right:", right500000)
    print("Trapezoid:", trap500000)
    leftErr[7] = abs(correct - left500000)
    rightErr[7] = abs(correct - right500000)
    trapErr[7] = abs(correct - trap500000)

    # N = 1000000:
    left1000000 = left(1000000, a, b)
    right1000000 = right(1000000, a, b)
    trap1000000 = trap(1000000, a, b)
    print("N = 1000000:")
    print("Left:", left1000000)
    print("Right:", right1000000)
    print("Trapezoid:", trap1000000)
    leftErr[8] = abs(correct - left1000000)
    rightErr[8] = abs(correct - right1000000)
    trapErr[8] = abs(correct - trap1000000)

    # N = 5000000:
    left5000000 = left(5000000, a, b)
    right5000000 = right(5000000, a, b)
    trap5000000 = trap(5000000, a, b)
    print("N = 5000000:")
    print("Left:", left5000000)
    print("Right:", right5000000)
    print("Trapezoid:", trap5000000)
    leftErr[9] = abs(correct - left5000000)
    rightErr[9] = abs(correct - right5000000)
    trapErr[9] = abs(correct - trap5000000)

    # N = 10000000:
    left10000000 = left(10000000, a, b)
    right10000000 = right(10000000, a, b)
    trap10000000 = trap(10000000, a, b)
    print("N = 10000000:")
    print("Left:", left10000000)
    print("Right:", right10000000)
    print("Trapezoid:", trap10000000)
    leftErr[10] = abs(correct - left10000000)
    rightErr[10] = abs(correct - right10000000)
    trapErr[10] = abs(correct - trap10000000)

    # N = 50000000:
    left50000000 = left(50000000, a, b)
    right50000000 = right(50000000, a, b)
    trap50000000 = trap(50000000, a, b)
    print("N = 50000000:")
    print("Left:", left50000000)
    print("Right:", right50000000)
    print("Trapezoid:", trap50000000)
    leftErr[11] = abs(correct - left50000000)
    rightErr[11] = abs(correct - right50000000)
    trapErr[11] = abs(correct - trap50000000)


    # Create the range of N values.
    N = [x for p in range(2, 8) for x in (10 ** p, 5 * (10 ** p))]

    # Create graphs of the left hand errors
    plt.figure()
    fig, leftError = plt.subplots()
    leftError.plot(N, leftErr)
    leftError.set_yscale('log')
    leftError.set_xscale('log')
    plt.title('Left Hand Riemann Sum Error for f(x) = cos(x/10)')
    plt.xlabel('Number of Subintervals')
    plt.ylabel('Absolute Error')
    plt.savefig('left.png', bbox_inches='tight')
    plt.close('all')

    # Create graphs of the right hand errors
    plt.figure()
    fig, rightError = plt.subplots()
    rightError.plot(N, rightErr)
    rightError.set_yscale('log')
    rightError.set_xscale('log')
    plt.title('Right Hand Riemann Sum Error for f(x) = cos(x/10)')
    plt.xlabel('Number of Subintervals')
    plt.ylabel('Absolute Error')
    plt.savefig('right.png', bbox_inches='tight')
    plt.close('all')

    # Create graphs of the trapezoid approximation errors
    plt.figure()
    fig, trapError = plt.subplots()
    trapError.plot(N, trapErr)
    trapError.set_yscale('log')
    trapError.set_xscale('log')
    plt.title('Trapezoidal Approximation Riemann Sum Error for f(x) = cos(x/10)')
    plt.xlabel('Number of Subintervals')
    plt.ylabel('Absolute Error')
    plt.savefig('trap.png', bbox_inches='tight')
    plt.close('all')


