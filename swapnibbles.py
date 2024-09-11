num = int(input("Enter a decimal number : "))

bits1 = []
bits2 = []

for i in range(0, 4):
    bits1.append(num >> i & 1)

for i in range(0, 4):
    bits2.append(num >> (4 + i) & 1)

for i in range(0, 4):
    print(bits2[i], end=" ")


for i in range(0, 4):
    print(bits1[i], end=" ")
print("")

for i in range(0, 4):
    print(bits1[i], end=" ")

for i in range(0, 4):
    print(bits2[i], end=" ")

print("")
