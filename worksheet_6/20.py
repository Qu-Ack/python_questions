def binary_search(arr, num):
    start = 0
    end = len(arr) - 1

    while start < end:
        middle = int((start + end) / 2)
        if arr[middle] == num:
            print(arr[middle])
            break
        elif arr[middle] > num:
            end = middle
            print(arr[start:end])
        elif arr[middle] < num:
            start = middle
            print(arr[start:end])


binary_search([1, 2, 3, 4, 5], 2)
