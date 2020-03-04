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

s1.discard(1)   # The only notable difference is, 
                # remove() will throw an error message when the element which 
                # we are trying to remove is not there in the set, whereas, 
                # discard() will not intimate the absence of element which we try to remove.
print(s1)

s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)

s1 = {1,2}
s2 = {1,2,3}
s3 = {5}

print(s1.isdisjoint(s2))    # It will return True if both sets have atleast 1 common element 
print(s1.isdisjoint(s3))    # It will return False as both sets have 0 common element 

print(s1.issubset(s2))
print(s2.issuperset(s1))

s1.add(4)
print(s1.symmetric_difference(s2))

print(s1.union(s2))
s1.update(s2)
print(s1)