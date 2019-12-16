#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
i = number % 10
if i > 5:
    print("Last digit of {} is {} and is gretaer than 5".format(number, i))
elif i == 0:
    print("Last digit of {} is 0 and is 0".format(number))
else:
     print("Last digit of {} is {} and is less than 6 and not 0".format(number, i))
