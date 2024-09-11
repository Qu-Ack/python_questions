str = input("Enter you input string : ")
start_index = int(input("Enter the position from which you want to extract : "))
character_num = int(input("How many characters do you want to extract : "))


def extraction(str, start_index, character_num):
    result = ""

    remaining_len = len(str) - start_index
    if character_num > remaining_len:
        print("EOS: End of string")
        exit()

    for i in range(start_index - 1, start_index - 1 + character_num):
        result += str[i]

    return result


print(extraction(str, start_index, character_num))
