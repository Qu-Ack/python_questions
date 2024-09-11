list_tuples = [
    ("dakshsangal@gmail.com", "Daksh Sangal"),
    ("dhruvtiwari@gmail.com", "Dhruv Tiwari"),
]


def angle_brackets(list_of_tuples):
    result = []
    str = ""
    for tup in list_of_tuples:
        str = f"<{tup[0]} {tup[1]}>"
        result.append(str)
        str = ""
    return result


result = angle_brackets(list_tuples)

for i in result:
    print(i)
