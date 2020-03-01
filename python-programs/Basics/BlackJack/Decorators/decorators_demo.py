print('---------------------------------------------------------')
def new_decorator(original_function):

    def wrap_function():
        print('Before calling original function()')
        original_function()
        print('After calling original function()')

    return wrap_function

def func_to_be_decorated():
    print('This needs to be decorated !')


decorated_func = new_decorator(func_to_be_decorated)
decorated_func()

print('---------------------------------------------------------')

@new_decorator
def callMe():
    print('callMe() called !')

callMe()

print('---------------------------------------------------------')
