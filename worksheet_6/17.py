alphabets = {}


def count_alphabets(my_str):
    my_str = my_str.lower()
    for alphabet in my_str:
        if alphabet == "" or alphabet == " ":
            continue
        if alphabet in alphabets:
            alphabets[alphabet] += 1
        else:
            alphabets[alphabet] = 1


count_alphabets("this is a test string")


for key, value in alphabets.items():
    print(f"{key}:{value}")
