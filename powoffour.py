num = int(input("Enter a decimal number : "))


bin_num = bin(num)[2:]


num_of_ones = 0
if num & (num - 1) == 0:
    count = 0
    while count < 8:
        count = count + 1
        num = num >> 2
        if num == 1:
            print("Power of Four")
            break
