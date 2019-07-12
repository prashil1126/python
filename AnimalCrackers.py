"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""


def animal_crackers(word):
    mylist = word.split()
    return mylist[0][0].lower() == mylist[1][0].lower()



print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))
