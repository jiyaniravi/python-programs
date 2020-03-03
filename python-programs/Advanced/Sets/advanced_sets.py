s = set()

s.add(1)
s.add(1)
s.add(1)
s.add(2)
s.add(2)
print(s)

s.clear()
print(s)

s = {1,2,3}
s_copy = s.copy()
print(s_copy)

s.add(4)
print(s)
print(s_copy)

print(s.difference(s_copy))

s1 = {1,2,3}
s2 = {2,4,5}
s1.difference_update(s2)
print(s1)

s1.discard(1)
print(s1)

s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)

