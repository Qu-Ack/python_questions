str = "Daksh Sangal"


def initials(str):

    split_str = str.split(" ")

    for word in split_str:
        print(word[0], end=" ")

    print("")


initials(str)
