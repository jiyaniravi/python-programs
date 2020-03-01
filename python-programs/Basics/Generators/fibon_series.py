def generator_fibbon(number):
    a = 1
    b = 1
    for n in range(number):
        yield a
        a,b=b,a+b

for n in generator_fibbon(10):
    print(n)