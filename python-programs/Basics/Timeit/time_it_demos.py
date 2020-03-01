import timeit

time_taken = timeit.timeit("'-'.join(str(i) for i in range(100))", number=10000)
print(time_taken)

time_taken = timeit.timeit("'-'.join([str(i) for i in range(100)])", number=10000)
print(time_taken)

time_taken = timeit.timeit("'-'.join(map(str, range(100)))", number=10000)
print(time_taken)