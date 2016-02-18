"""
File: <interest_rate.py>

Copyright (c) 2016 <Lucas Blair>

License: MIT

<calculates interest rate after n years>
"""
from math import pow
A = 1000
n = 3
p = 5.0
amount = A * pow ((1 + (p / 100)), n)
print amount
