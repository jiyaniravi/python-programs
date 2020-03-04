l = [1,2,3]

l.append(4)

print(l)
print(l.count(5))
print(l.count(1))

# Notice difference between append and extend APIs
x = [1,2,3]
x.append([4,5])
print(x)

x = [1,2,3]
x.extend([4,5])
print(x)

print(l.index(3))   # index starts from 0
#print(l.index(10)) # ValueError: 10 is not in list

l.insert(2,'inserted')  # At what index, what we have to add
print(l)

element = l.pop()   # Pops last element from list
print(element)

element = l.pop(2)  # Pops element from specific index of list
print(element)

l = [1,2,3,4,2,3]
l.remove(3)         # remove will remove first occurence of 3 from list
print(l)

l.reverse()
print(l)

l.sort()
print(l)