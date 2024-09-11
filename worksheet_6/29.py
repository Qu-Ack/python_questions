myList = []
for i in range(1, 101):
    myList.append(i)


for i in range(1, len(myList)):
    for j in range(i + 1, len(myList)):
        if myList[i] != 0:
            if myList[j] % myList[i] == 0:
                myList[j] = 0


for i in myList:
    if i != 0:
        print(i, end=" ")
print("")
