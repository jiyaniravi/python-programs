import re

my_lyrics = '''On the first day of Christmas my true love sent to me
A partridge in a pear tree
On the second day of Christmas my true love sent to me
2 turtle doves
And a partridge in a pear tree
On the third day of Christmas my true love sent to me
3 French hens, two turtle doves
And a partridge in a pear tree
On the fourth day of Christmas my true love sent to me
4 calling birds, three French hens, two turtle doves
And a partridge in a pear tree
On the fifth day of Christmas my true love sent to me
5 gold rings, four calling birds, three French hens, two turtle doves
And a partridge in a pear tree
On the sixth day of Christmas my true love sent to me
6 geese a laying, five gold rings, four calling birds
Three French hens, two turtle doves'''

pattern = re.compile(r'\d+\s\w+')

print(pattern.findall(my_lyrics))
