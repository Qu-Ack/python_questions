n = int(input("enter the number of elements: "))


my_list = []
for i in range(0, n):
    num = int(input(f"Enter the {i} element : "))
    my_list.append(num)

for x in range(0, n):
    new_list = []
    for i in range(0, len(my_list) - 1):
        diff = my_list[i + 1] - my_list[i]
        new_list.append(diff)

    my_list = new_list
    print(new_list)
