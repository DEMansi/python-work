#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

from decimal import *
data = list(map(Decimal, '9.45 2.79 0.45 3.50 1.00 0.01 7.25 0.76 0.24'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))
