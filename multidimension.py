x = int(input("enter the first order of the matrix: "))
y = int(input("Enter the second order of the matrix: "))
matrix = []

for i in range(0, x):
    a = []
    for j in range(0, y):
        num = int(input("Enter the first number: "))
        a.append(num)
    matrix.append(a)

for i in range(0, x):
    for j in range(0, y):
        print(matrix[i][j], end=" ")
    print("")
