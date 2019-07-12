"""

PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
"""


def paper_doll(mystring):
    new_string = ""
    for item in mystring:
        new_string += item*3
    return new_string


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
