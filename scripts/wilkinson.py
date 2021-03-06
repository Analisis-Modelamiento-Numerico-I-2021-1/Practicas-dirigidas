#!/usr/bin/python

from sympy.abc import x
import sympy

f = (x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9)*(x-10)*(x-11)*(x-12)*(x-13)*(x-14)*(x-15)*(x-16)*(x-17)*(x-18)*(x-19)*(x-20)

print(f.diff())

print(f.diff().evalf(subs={x:20}))

print(sympy.factorial(19))

print(sympy.factorial(19) - f.diff().evalf(subs={x:20}))

# (1)*(2)*(3)*(4)*(5)*(6)*(7)*(8)*(9)*(20 - 10)*(20 - 9)*(20 - 8)*(20 - 7)*(20 - 6)*(20 - 5)*(16)*(17)*(18)*(19)