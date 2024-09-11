def n_join(my_str, arr):
    result = my_str
    for i in arr:
        result = result + str(i)
    return result


my_str = n_join("DakshSangal", [1, 2, 3])

print(my_str)
