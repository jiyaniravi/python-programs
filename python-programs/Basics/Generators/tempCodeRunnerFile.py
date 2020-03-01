def create_cube(n):
    for x in range(0, n):
        yield x+3

for a in (create_cube(10000)):
    print(a)