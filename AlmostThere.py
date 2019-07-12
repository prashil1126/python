"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""


def almost_there(num):
    if abs(num-100) <= 10 or abs(num-200) <= 10:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(140))
print(almost_there(209))
