userString = input("Enter a string: ")

noOfDigits = noOfUpper = noOfLower = 0
noOfWords = 1

for i in range(len(userString)):
    if userString[i].isdigit():
        noOfDigits += 1
    if userString[i].isspace():
        noOfWords += 1
    if userString[i].isupper():
        noOfUpper += 1
    if userString[i].islower():
        noOfLower += 1

print(
    f"The user input contains {noOfWords} words with {noOfDigits} Digits, {noOfUpper} Uppercase letters and {noOfLower} lowercase letters")
