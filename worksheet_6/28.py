def duplicates_list(arr):
    uniqueList = []
    for i in arr:
        if i in uniqueList:
            print(i)
        else:
            uniqueList.append(i)


duplicates_list(["daksh", "daksh", "sangal", "sangal", "world"])
