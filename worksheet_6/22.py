def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
            print(arr)


my_arr = [32, 31, 30, 8, 1, 102]

bubble_sort(my_arr)

print(my_arr)
