"""

MASTER YODA: Given a sentence, return a sentence with the words reversed
"""


def master_yoda(mystring):
    my_list = mystring.split()
    my_list = my_list[::-1]
    new_str = " ".join(my_list)
    return new_str


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
