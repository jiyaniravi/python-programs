from collections import defaultdict

normal_dict = {'k1':'value1', 'k2':'value2'}
print(normal_dict['k1'])
print(normal_dict['k2'])
#print(normal_dict['k3']) #This line will throw KeyError as k3 is not available in normal dictionary

mdd = defaultdict(object)
print(mdd['k1'])
mdd = defaultdict(int)
print(mdd['k1'])

mdd = defaultdict(lambda : 10)
print(mdd['k1'])