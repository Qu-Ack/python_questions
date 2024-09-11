import sys

stri = ""

while True:
    char = sys.stdin.read(1)
    stri = stri + char
    if char == "\x03":
        break
    elif char == "\r":
        stri = stri + "\n"


print(stri)


def my_splitlines(stri_test, keepends=False):
    arr = []
    stri = ""
    for char in stri_test:
        if char == "\n":
            if keepends:
                stri = stri + char
                arr.append(stri)
                stri = ""
            else:
                arr.append(stri)
                stri = ""
        else:
            stri = stri + char

    return arr


new_arr = my_splitlines(stri, True)


for i in new_arr:
    print(i)
