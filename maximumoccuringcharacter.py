str = "tdaskdsh"

char_map = {}


for character in str:
    if character in char_map:
        char_map[character] += 1
    else:
        char_map[character] = 1

max = 0
maxchar = None
for key, value in char_map.items():
    if key != " ":
        if value > max:
            max = value
            maxchar = key


print(maxchar)
