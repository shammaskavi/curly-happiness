# 1b. Find the Palindrom and the number of instances of every number
# The Shammaskavi Way
val = int(input("Enter a value : "))
stringVal = str(val)
if stringVal == stringVal[::-1]:
    print("Entered Value is Palindrome")
    for i in range(10):
        if stringVal.count(str(i)) > 0:
            print(str(i), "appears", stringVal.count(str(i)), "times")
else:
    print("Entered Value is Not a Palindrome")


# The other way: 
# num = int(input("Enter the number to be checked for palindrome: "))
# temp = num
# rev = 0

# while(num > 0):
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10

#     if(temp == rev):
#         print(f"The given number {num} is palindrome.")
#     else: 
#         print(f"The given number {num} is not a palindrome")
    