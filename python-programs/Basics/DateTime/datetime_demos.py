import datetime

def print_line():
    print('----------------------------------------------')

print_line()

t_obj = datetime.time(5,5,55)
print(t_obj)

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

print_line()

d_obj = datetime.date.today()
print(d_obj)
print(d_obj.year)
print(d_obj.month)
print(d_obj.day)
print(d_obj.weekday())
print(d_obj.resolution)
print(d_obj.timetuple())

print_line()

d1 = datetime.date(2020, 2, 29)
print(d1)
d2 = d1.replace(year=1920)
print(d2)

print(d1-d2)

print_line()