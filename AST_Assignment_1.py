'''Write a Java program which performs the following tasks:
1. It first inputs an integer between 1 and 100 from the user. Let's assume the user inputs n.
2. It then reads n more integers and stores them.
3. It computes the sum, the product, the average, the variance, the smallest and the largest
value of these numbers.
4. It outputs, in a nicely formatted way, all the numbers input and the statistics computed.
Note: The output should also be integers, i.e. if the user input three numbers which sum up to
13, the average computed should be 4, not 4.3333...'''

from __future__ import division
import numpy as np
import math
from decimal import Decimal as D
from decimal import getcontext

#desired_values = int(input("Please insert a number from 1 to 100"))
#string_values = raw_input("Please insert different values separated by comma")

def input_from_user(values):
    return  [int(str_int) for str_int in values.split(',')]

#organized = input_from_user(values)

def sum_numbers (list_numbers):
    sum=0
    for i in list_numbers:
        sum += i
    return sum

def low_high_number (list_numbers):
    mini=1e50
    maxi=-1e50
    for i in list_numbers:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
    return mini,maxi

def variance_number(list_numbers):
    return np.var(list_numbers)

def average_number (list_numbers):
    return (sum_numbers(list_numbers)/len(list_numbers))

#print("The sum of numbers is equal to: ",sum_numbers(organized))
#print("The lowest numbers is equal to: ", low_high_number (organized)[0])
#print("The biggest number is equal to: ", low_high_number (organized)[1])
#print("The variance number is equal to: ",variance_number(organized))
#print("The average is equal to: ",average_number(organized))

"""Write a Java program which performs the following tasks:
1. It finds all prime numbers between 0 and the largest integer, and between 0 and the largest
long integer.
2. It determines the time needed to count from the smallest to the largest integer, and the
smallest long to the largest long integer.
3. It outputs, in a nicely formatted way, all the numbers computed."""


import timeit
from decimal import Decimal

#print("Find all the prime numbers between 0 and your largest integer")
def primes(min, max):
    pp = []
    if max >= 2 >= min:
        pp.append(2)
    primes = [2]
    i = 3
    while i <= max:
        for p in primes:
            if i % p == 0 or p*p > i:
                break
        if i % p != 0:
            primes.append(i)
            if i >= min:
                pp.append(i)
        i += 2
    return pp

#primes(0,low_high_number (organized)[1])

def count_int():
    start = timeit.default_timer()
    counting = 0
    for i in range(0,255):
        counting += i
        stop = timeit.default_timer()
    return stop-start

#print("The amount of time to test from the smallest to the largest integer is equal to: ",count_int())

#Use it with caution because python does not have a limit for long values for 100000000 numbers it takes 26.8 seconds to solve
def count_long():
    start = timeit.default_timer()
    counting = 0
    for i in range(0,1000000):
        counting += i
        stop = timeit.default_timer()
    return stop-start
#print("The amount of time to test from the smallest to the largest integer is equal to: ",count_long())

"""Write an application that iterates over positive integers from 0 to 100, calculates various functions
in n as listed below, and outputs the results (as integer, where possible and sensible) in table
format, each function value in a separate column.
f(n) = 2n
f(n) = n^(1/2)
f(n) = 10^n
f(n) = n^3
f(n) = 2^(1/n)
f(n) = e^n
Some function values may exceed the range of commonly used variable types. Think of alternative
ways of representating or calculating them in this case."""
import math
def different_functions(initial_value,final_value):
    my_range=range(initial_value,final_value)
    function_1 = [2*integer for integer in my_range]
    function_2 = [integer**(.5) for integer in my_range]
    function_3 = [10**integer for integer in my_range]
    function_4 = [integer**3 for integer in my_range]
    function_5 = [2^(1/integer) for integer in my_range]
    function_6 = [math.exp(integer) for integer in my_range]
    for i in my_range:
        if i == len(my_range):
            break
        else:
            print("| {0:.2f} \t| {1:.2f} \t| {2:.5E} \t| {3:.2f} \t| {2:.5E} \t| {3:.2f} \t|".format(function_1[i],function_2[i],function_3[i],function_4[i],function_5[i],function_6[i]))

#different_functions(1,101)

'''Write a program that inputs the diameter of a circle as a number x from the user and outputs
the circumference and the area of the circle.
Then extend your program such that it demonstrates the effect of approximating n, as follows:
. It asks the user to input the maximum precision (number of digits after the period) of n
to be considered.
. Check if this number is reasonable. Otherwise take the maximum reasonable number.
. Approximate by iterating over the the number of digits of precision for n, i.e. in the first
iteration n is approximated by 3, in the second iteration by 3.1, then 3.14, and so forth.
The program should cut off n after the current precision length, not round it!
. Do this until the maximum number of digits of precision is reached, and give the percentage
of increase of the circumference and the area over the previous iteration.'''


def input_diameter():
    diameter = int(input("Please insert a desired diameter for a circle"))
    return diameter

#input_diameter = input_diameter()

def circle_function(diameter,pi):
    diameter_in_float = D(diameter)
    pi_in_float = D(pi)
    circumference = pi_in_float*diameter_in_float
    area = pi_in_float*(diameter_in_float/2)**2
    return (circumference),(area)


#circle_data = circle_function(input_diameter,math.pi)

def get_pi(max):
    #https://www.math.hmc.edu/funfacts/ffiles/20010.5.shtml
    getcontext().prec = max+1
    iteration = 10000
    pi = D(0)
    for k in range(iteration):
        pi += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
    return pi
#print(get_pi(25))

def input_desired_digits():
    precision = int(input("Please select how many digits do you like to take in consideration (please be reasonable)"))
    default_precision = 15
    if precision > default_precision:
        precision = default_precision
        print("You wasn't reasonable a default value {0} will be used".format(default_precision))
    return precision

def extend_circle_function(precision):
    result_list = []

    for i in range(precision+1):
        if i == 0:
            calculated_pi = 3
            result_list.append(circle_function(3,3))
        else:
            calculated_pi = get_pi(i)
            result_list.append(circle_function(3,calculated_pi))
            circumference_perc_growth = ((result_list[i][0] - result_list[i-1][0])/(result_list[i-1][0]))*100
            area_perc_growth = ((result_list[i][1] - result_list[i-1][1])/(result_list[i-1][1]))*100
            print("The percentage of growth of the circumference is = : ",circumference_perc_growth)
            print("The percentage of growth of the area is = : ",area_perc_growth )

#extend_circle_function(input_desired_digits())


#### Test Cases ###

def sum_numbers_test():
    assert sum_numbers([]) == 0
    assert sum_numbers([4, 5]) == 9
    assert sum_numbers([-6, 6, -7, 3]) == -4
    assert sum_numbers([0, 0, 0]) == 0
    assert sum_numbers([10000000000000, 1, 5]) == 10000000000006

def low_high_number_test():
    assert low_high_number([1, 1]) == (1, 1)
    assert low_high_number([10, 10, 1, 5, 3]) == (1, 10)
    assert low_high_number([-1, -1]) == (-1, -1)
    #assert low_high_number([]) == (0, 0)

def variance_number_test():
    assert variance_number([12, 2]) == np.var([12, 2])
    assert variance_number([0, 0, 0]) == np.var([0, 0, 0])
    assert variance_number([-14, 34]) == np.var([-14, 34])
    assert variance_number([3, 3, 3]) == np.var([3, 3, 3])

def average_number_test():
    assert average_number([12, 2]) == np.average([12, 2])
    assert average_number([0, 0, 0]) == np.average([0, 0, 0])
    assert average_number([-14, 34]) == np.average([-14, 34])
    assert average_number([3, 3, 3]) == np.average([3, 3, 3])

def primes_test():
    assert primes(0, 3) == [2, 3]
    assert primes(3, 0) == []
    assert primes(0, 2) == [2]
    assert primes(-7, -7) == []

def count_int_test():
    assert count_int() > 0

def count_long_test():
    assert count_long() > 0

def count_long_test():
    assert count_long() > 0

def circle_function_test():
    #assert circle_function(0, 3.14) == float(0)
    #assert circle_function(1, 3.14) == float(3.14)
    #assert circle_function(-10, 3.14) == float(0)
    #assert circle_function(0, 0) == float(0)

sum_numbers_test()
low_high_number_test()
variance_number_test()
average_number_test()
primes_test()
count_int_test()
count_long_test()
circle_function_test()
