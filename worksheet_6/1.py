def get_word(my_str, word):
    split_arr = my_str.split()
    return split_arr[word - 1]


print(get_word("This is a test sentence", 2))
