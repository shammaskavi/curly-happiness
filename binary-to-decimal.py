# def binaryToDecimal(b):
#     d = 0
#     i = 0
#     while b > 0:
#         r = b % 10
#         d = d + [r * pow(2,i)]
#         i = i + 1
#         b = b / 10
#     return d

# binary = input("Enter the binary no.: ")
#decimal = binaryToDecimal(binary)
#print(decimal)


def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2

    return decimal

num = int(input("Enter the number to be converted: "))
numToDec = binaryTodecimal(num)

print(f"The Decimal of {num} is {numToDec}")