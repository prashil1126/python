"""
LESSER OF TWO EVENS: Write a function that returns the 
lesser of two given numbers if 
both numbers are even, but returns the greater if one or both numbers are odd
"""


def even_odd(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


c = even_odd(2, 4)
d = even_odd(2, 5)
print(c, "\n", d)
