class PaliStr:
    def __init__(self):
        self.isPali = False
    def checkPalindrome(self, my_str):
        return my_str == my_str[::-1]
        
class PaliInt(PaliStr):
    def __init__(self):
        self.isPali = False

    def checkPalindrome(self, val):
        temp = val
        rev = 0
        while temp != 0:
            dig = temp % 10
            rev = (rev * 10) + dig
            temp = temp // 10
        return val == rev


st = input("Enter a string: ")
stObj = PaliStr()
if stObj.checkPalindrome(st):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")

val = int(input("Enter an integer: "))
intObj = PaliInt()
if intObj.checkPalindrome(val):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")
