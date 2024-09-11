x = int(input("Enter the number of columns: "))
y = int(input("Enter the number of rows : "))


matrix = []


for i in range(0, x):
    a = []
    for j in range(0, y):
        num = int(input(f"Enter the {j} number : "))
        a.append(num)
    matrix.append(a)


for i in range(0, x):
    for j in range(0, y):
        print(matrix[i][j], end=" ")
    print("")


print("new list")


matrix2 = [[x**3 for x in it if x % 2 == 0 else x] for it in matrix]


for i in range(0, len(matrix2)):
    for j in range(0, len(matrix2[i])):
        print(matrix2[i][j], end=" ")
    print("")
