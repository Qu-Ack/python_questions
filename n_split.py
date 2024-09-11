import math

user_string = input("enter the string: ")


def n_split(user_string, seperator, partition_limit=math.inf):
    arr = []
    stri = ""
    part = partition_limit

    for char in user_string:
        if part > 0:
            if char == seperator:
                arr.append(stri)
                part = part - 1
                stri = ""
            else:
                stri = stri + char
        else:
            stri = stri + char

    if stri != "":
        arr.append(stri)

    return arr


new_arr = n_split(user_string, " ")


for i in new_arr:
    print(i)
