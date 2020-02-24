try:
    number = 10+'10'
except:
    print('Exception occured !')
else:
    print('Else part got called !')
finally:
    print('Finally always gets called !')

print('#####################################################')

try:
    number = 10+11
except:
    print('Exception occured !')
else:
    print('Else part got called !')
finally:
    print('Finally always gets called !')

print('#####################################################')

try:
    f = open('test.txt','r')
    f.write('This is simple text !')
except TypeError:
    print('Type error got caught !')
except OSError:
    print('OS error got caught !')
else:
    print('Else got caught')
finally:
    print('I will get executed !')

print('#####################################################')

def ask_for_int():
    while True:
        try:
            number = int(input('Please enter number : '))
        except:
            print('Entered value is in correct !')
            continue
        else:
            print('Thanks for providing correct value !')
            break
        finally:
            print('End of function')

ask_for_int()

print('#####################################################')

