#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastd = number % 10
else:
    lastd = ((number * -1) % 10) * -1

if lastd == 0:
    print(f"Last digit of {number} is {lastd} and is 0")
elif lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
else:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")