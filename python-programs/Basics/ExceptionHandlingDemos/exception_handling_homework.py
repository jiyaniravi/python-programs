print('###########################################################')

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('TypeError got caught !')
else:
    print('No exception occured !')

print('###########################################################')

try:
    x = 5 
    y = 0
    z = x/y
except ZeroDivisionError as ZDError:
    print('ZeroDivisionError got caught !')
else:
    print('No exception occured !')

print('###########################################################')

def squareNumber():
    while True:
        try:
            number = int(input('Input an integer : '))
            print('Thank you, your number squared is : '+str(number**2));
            break
        except ValueError:
            print('An error occured! Please try again.')

squareNumber()