my_normal_dict = {}
my_normal_dict['a']=1
my_normal_dict['b']=2
my_normal_dict['c']=3
my_normal_dict['d']=4
my_normal_dict['e']=5
my_normal_dict['f']=6
my_normal_dict['g']=7
my_normal_dict['h']=8
my_normal_dict['i']=9
my_normal_dict['j']=10

# After python 3.6 normal dictionary preserves insertion order !
# https://docs.python.org/3.6/whatsnew/3.6.html#other-language-changes
for k,v in my_normal_dict.items():
    print (k,v)

