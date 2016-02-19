"""
File: <sin2_plus_cos2.py>

Copyright (c) 2016 <Lucas Blair>

License: MIT

<Calculates a sin and cos formula accurately>
"""
#Problem A.)
from math import sin, cos, pi
x = pi/4
sumSquares = (sin(x) * sin(x)) + (cos(x) * cos(x))
print sumSquares

#Problem B.)
from math import pow
v = 3
t = 1
a = 2
s = v * t + (0.5 * a * pow(t,t))
print s

#Problem C.)
a = 3.3
b = 5.3
a2 = a*a
b2 = b*b

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b) * (a + b)
eq2_pow = (a - b) * (a - b)

if eq1_sum == eq1_pow:
    print "Equation confirmed!"

if eq2_sum == eq2_pow:
    print "Equation confirmed!"
