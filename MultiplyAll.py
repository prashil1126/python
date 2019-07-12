def mul(a):
    product = 1
    for item in a:
        product *= item
    return product


print(mul([1, 2, 3, -4]))
