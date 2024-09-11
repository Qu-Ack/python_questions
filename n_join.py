stri = input("enter the string : ")
num = int(input("Enter the number of elements: "))
arr = []

for i in range(0, num):
    n = int(input("Enter the number : "))
    arr.append(n)


def n_join(arr, stri):
    for i in range(0, len(arr)):
        stri = str(stri) + str(arr[i])
    return stri


print(n_join(arr, stri))
