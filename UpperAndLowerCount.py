def upper_lower(my_string):
    upper_num = 0
    lower_num = 0
    for item in my_string:
        if str(item).islower():
            lower_num += 1
        elif str(item).isupper():
            upper_num += 1
        else:
            continue
    print("Number of upper case characters = ", upper_num)
    print("Number of upper case characters = ", lower_num)


upper_lower("Hello Mr. Rogers, how are you this fine Tuesday?")

