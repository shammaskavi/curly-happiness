# Search for phone number and email in a file 
import re

phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')


with open('example.txt', 'r') as f:
    for line in f:
        phone_matches = phone_regex.findall(line)
        for match in phone_matches:
            print("Phone number:", match)
        email_matches = email_regex.findall(line)
        for match in email_matches:
            print("Email:", match)
