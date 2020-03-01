def line_saperator():
    print('--------------------------------------------------')

def simple_generator():
    for n in range(2):
        yield n

for n in simple_generator():
    print(n)

line_saperator()

g = simple_generator()
print(next(g))
print(next(g))
#print(next(g)) : This line will cause below error
#
#Traceback (most recent call last):
#  File "d:\Knowledge\Python\git\python-programs\Basics\Generators\iterate_generator.py", line 13, in <module>
#    print(next(g))
#StopIteration
line_saperator()

hello_str = 'hello'
i = iter(hello_str)
print(next(i))
print(next(i))
print(next(i))

line_saperator()