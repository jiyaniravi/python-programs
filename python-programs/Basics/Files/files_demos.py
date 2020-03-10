import os

def new_decorator(original_function):
    def wrap_function():
        print('----------------------------------------------')
        original_function()
        print('----------------------------------------------')
    return wrap_function

print(os.sep)       # OS separator 
print(os.getcwd())  # Current working directory

original_cwd = os.getcwd()
os.chdir('D:\\')
print(os.getcwd())  # Current working directory

os.chdir(original_cwd)
print(os.path.abspath('CSMResult.PNG'))

print(os.path.relpath('CSMResult.PNG'))

print(os.path.exists('CSMResult.PNG'))
