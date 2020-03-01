import datetime
from profiler import profile

start_1 =  datetime.datetime.now()
start_2 =  datetime.datetime.now()
finish_1 =  datetime.datetime.now()
finish_2 = datetime.datetime.now()

def with_generator():
    start_1 = datetime.datetime.now()
    def create_cube(n):
        for x in range(0, n):
            yield x+3

    for a in (create_cube(100000)):
        a+=a
    finish_1 = datetime.datetime.now()
    print('Time taken by generator : '+str(finish_1-start_1))

def without_generator():
   
    def normal_create_cube(n):
        start_2 = datetime.datetime.now()
        arr = []
        for x in range(0, n):
            arr.append(x+3)
        return arr

    for a in (normal_create_cube(100000)):
        a+=a
        finish_2 = datetime.datetime.now()
    print('Time taken without generator : '+str(finish_2-start_2))

run_profiling1 = profile(with_generator)
run_profiling2 = profile(without_generator)

run_profiling1()
run_profiling2()