import shelve

my_shelf = shelve.open("mydata")
my_shelf['Bitches'] = ['Dholi','Kali']
my_shelf.close()

my_shelf = shelve.open("mydata")
print(my_shelf['Bitches'])
my_shelf.close()