"""

BLACKJACK: Given three integers between 1 and 11, if
their sum is less than or equal to 21, return their sum. If their sum exceeds 21
and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
"""


def blackjack(a, b, c):
    d = a + b + c
    if d > 21:
        if a == 11 or b == 11 or c == 11:
            d -= 10
            if d > 21:
                return "BUST"
            else:
                return d
        else:
            return "BUST"
    else:
        return d


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
