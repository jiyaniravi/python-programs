from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(2, 'American', 'Sam')
print(sam.name+' : '+sam.breed+' : '+str(sam.age))

print(sam.count('Sam'))
print(sam.index('Sam'))