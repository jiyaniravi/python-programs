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
