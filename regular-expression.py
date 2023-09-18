import re

def is_phone_number(numStr):
    """All these functions, and still you couldn't get her number"""
    if len(numStr) != 12:
        return False
    for i in range(len(numStr)):
        if i == 3 or i == 7:
            if numStr[i] != "-":
                return False
        else:
            if not numStr[i].isdigit():
                return False
    return True

def check_phone_number(numStr):
    """Enter a witty comment about the function"""
    phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(phone_number_pattern.match(numStr))

ph_num = input("Enter a phone number: ")

print("Without using Regular Expression")
if is_phone_number(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression")
if check_phone_number(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
