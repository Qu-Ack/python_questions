def skip_elements(arr):
    result = []
    for i in range(0, len(arr)):
        if i % 2 == 0:
            result.append(arr[i])
    return result


result = skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])

print(result)
