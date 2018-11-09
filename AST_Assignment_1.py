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


"""Write a Java program which performs the following tasks:
1. It finds all prime numbers between 0 and the largest integer, and between 0 and the largest
long integer.
2. It determines the time needed to count from the smallest to the largest integer, and the
smallest long to the largest long integer.
3. It outputs, in a nicely formatted way, all the numbers computed."""




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
