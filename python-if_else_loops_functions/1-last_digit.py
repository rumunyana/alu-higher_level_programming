#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10
if number < 0:
    dig = dig * (-1)

if dig == 0:
    print(f"Last digit of {number} is {dig} and is 0")
elif dig > 5:
    print(f"Last digit of {number} is {dig} and is greater than 5")
else:
    print(f"Last digit of {number} is {dig} and is less than 6 and not 0")
