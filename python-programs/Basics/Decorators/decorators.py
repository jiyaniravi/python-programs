def printLine():
    print('#################################################')


printLine()

print('Function assignment ! :')
def func1():
    print('This is function 1 !')

func2 = func1
del func1
func2()

printLine()

print('Function within function and return ! :')
def hello(name = 'Ravi'):
    print('Hello function got called ! : ')
    def greet():
        return '\t This is greet function within hello()'
    def welcome():
        return '\t This is welcome function within hello()'
    if name == 'Ravi':
        return greet
    else:
        return welcome
my_new_func = hello('Aakash')
print(my_new_func())

printLine()

print('Passing a function as an argument ! :')
def functionReturn():
    return '\t functionReturn() got called !'

def callMain(outer_function):
    print('callMain() called !')
    print(outer_function())
callMain(functionReturn)

printLine()