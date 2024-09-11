vowels = "aeiou"
str = input("Enter the string : ")

occurances = 0
for i in range(0, len(str) - 1):
    if (str[i] in vowels) and (str[i + 1] in vowels):
        occurances += 1


print(occurances)
