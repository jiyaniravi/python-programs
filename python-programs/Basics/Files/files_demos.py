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


totalSize = 0
print(os.listdir())

for fileName in os.listdir():
    current_file = os.path.join("D:\\Knowledge\\Python\\git\\python-programs",fileName)
    print('current file : '+current_file)
    if os.path.isfile(current_file):
        continue
    else:
        totalSize+=os.path.getsize(current_file)

print(totalSize)

os.makedirs("D:\\Knowledge\\Python\\git\\python-programs\\Basics\\Files\\TestFolder1\\TestFolder2")