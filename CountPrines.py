"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
"""


def count_prime(my_num):
    prime = []
    for num in range(2, my_num + 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    return len(prime)


print(count_prime(100))
