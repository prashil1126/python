"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""


def old_mcdonald(mystring):
   first_half = mystring[:3]
   second_half = mystring[3:]
   return first_half.capitalize()+second_half.capitalize()



print(old_mcdonald("ramanand"))
