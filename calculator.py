#https://github.com/dem2131/lab10-DM-JL.git
# Partner 1: David Miller
# Partner 2: Jacob Lindland

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order. lab10-DM-JL
"""
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a
def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid arguments")
    return math.log(b) / math.log(a)

def exp(a, b):
    return a ** b