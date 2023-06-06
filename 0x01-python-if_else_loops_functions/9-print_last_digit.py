#!/usr/bin/python3
def print_last_digit(number):
    lastD = abs(number) % 10
    print(lastD, end="")
    return lastD
