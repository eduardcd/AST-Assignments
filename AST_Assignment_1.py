'''Write a Java program which performs the following tasks:
1. It first inputs an integer between 1 and 100 from the user. Let’s assume the user inputs n.
2. It then reads n more integers and stores them.
3. It computes the sum, the product, the average, the variance, the smallest and the largest
value of these numbers.
4. It outputs, in a nicely formatted way, all the numbers input and the statistics computed.
Note: The output should also be integers, i.e. if the user input three numbers which sum up to
13, the average computed should be 4, not 4.3333...'''

import numpy as np

desired_values = int(input("Please insert a number from 1 to 100"))
string_values = raw_input("Please insert different values separated by comma")

def input_from_user(values):
    return  [int(str_int) for str_int in values.split(',')]

organized = input_from_user(values)

def sum_numbers (list_numbers):
    sum=0
    for i in list_numbers:
        sum += i
    return sum

def low_high_number (list_numbers):
    mini=1e50
    maxi=-1e50
    for i in organized:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
    return mini,maxi

def variance_number(list_numbers):
    return np.var(organized)

def average_number (list_numbers):
    return (sum_numbers(organized)/len(organized))

print("The sum of numbers is equal to: ",sum_numbers(organized))
print("The lowest numbers is equal to: ", low_high_number (organized)[0])
print("The biggest number is equal to: ", low_high_number (organized)[1])
print("The variance number is equal to: ",variance_number(organized))
print("The average is equal to: ",average_number(organized))

"""Write a Java program which performs the following tasks:
1. It finds all prime numbers between 0 and the largest integer, and between 0 and the largest
long integer.
2. It determines the time needed to count from the smallest to the largest integer, and the
smallest long to the largest long integer.
3. It outputs, in a nicely formatted way, all the numbers computed."""


import timeit
from decimal import Decimal

print("Find all the prime numbers between 0 and your largest integer")
def primes(min, max):
    if max >= 2 >= min:
        print (2)
    primes = [2]
    i = 3
    while i <= max:
        for p in primes:
            if i % p == 0 or p*p > i:
                break
        if i % p != 0:
            primes.append(i)
            if i >= min:
                print (i)
        i += 2

primes(0,low_high_number (organized)[1])

def count_int():
    start = timeit.default_timer()
    counting = 0
    for i in range(0,255):
        counting += i
        stop = timeit.default_timer()
    return stop-start

print("The amount of time to test from the smallest to the largest integer is equal to: ",count_int())

#Use it with caution because python does not have a limit for long values for 100000000 numbers it takes 26.8 seconds to solve
def count_long():
    start = timeit.default_timer()
    counting = 0
    for i in range(0,1000000):
        counting += i
        stop = timeit.default_timer()
    return stop-start
print("The amount of time to test from the smallest to the largest integer is equal to: ",count_long())



'''Write a program that inputs the diameter of a circle as a number x from the user and outputs
the circumference and the area of the circle.
Then extend your program such that it demonstrates the effect of approximating π, as follows:
• It asks the user to input the maximum precision (number of digits after the period) of π
to be considered.
• Check if this number is reasonable. Otherwise take the maximum reasonable number.
• Approximate by iterating over the the number of digits of precision for π, i.e. in the first
iteration π is approximated by 3, in the second iteration by 3.1, then 3.14, and so forth.
The program should cut off π after the current precision length, not round it!
• Do this until the maximum number of digits of precision is reached, and give the percentage
of increase of the circumference and the area over the previous iteration.'''
