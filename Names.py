str = input("Enter Your Full Name: ")


def nameInitials(str):
    new_str = str.split(" ")
    for i in range(0, len(new_str)):
        if i == len(new_str) - 1:
            print(new_str[i])
        else:
            print(new_str[i][0], end=".")


nameInitials(str)
