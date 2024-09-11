vowels = "aeiou"


str = "this is a test"
result = ""


for character in str:
    if character in vowels:
        continue
    else:
        result += character


print(result)
