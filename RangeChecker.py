def range_check(a, b, c):
    return b in range(a, c+1)


print(range_check(3, 1, 10))
print(range_check(2, 5, 10))