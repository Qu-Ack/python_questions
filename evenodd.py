num = int(input("Enter a decimal number"))

bin_num = bin(num)[2:]


print(bin_num)

len_bin_num = len(bin_num)

if bin_num[len_bin_num - 1] == "0":
    print("EVEN")
else:
    print("ODD")
