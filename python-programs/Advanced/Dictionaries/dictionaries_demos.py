d = {'k1':1, 'k2':2}
print({x:x**2 for x in range(10)})

# Dictionary comprehensions 
print({k:v**2 for k,v in zip(['a','b'],range(2))})

# In Python 3.x, iteritems is no longer supported, Use items() instead
for k in d.items(): 
    print(k)

# In Python 3.x, iteritems is no longer supported, Use items() instead
for v in d.values():
    print(v)
