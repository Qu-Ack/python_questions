n = int(input("Enter the amounts of word : "))
word_list = []
synonyms = []
word_dict = {}
m = int(input("Enter the amount of synonyms for each word : "))
for i in range(0, n):
    word = input("Enter the word : ")
    word_dict[word] = []
    for x in range(0, m):
        synonym = input(f"Enter the synonym for {word}: ")
        word_dict[word].append(synonym)


for key, value in word_dict.items():
    print(f"{key}:{value}")
