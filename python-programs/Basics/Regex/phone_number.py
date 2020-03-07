import re

def isPhoneNumber(number):
    #pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d',)
    pattern = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}')
    match = pattern.search(number)
    print(match.group())

def searchPhoneNumbers(message):
    pattern = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}')
    return pattern.findall(message)

isPhoneNumber('123-115-1151')
list_phoneNumbers = searchPhoneNumbers('''This is message ! This is my first phone number : 123-456-7894 
If I am not available on this number, please call me on my home number : 789-456-1235
''')

print(list_phoneNumbers)
print(len(list_phoneNumbers))
