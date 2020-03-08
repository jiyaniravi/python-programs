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

pattern = re.compile(r'.at')
print(pattern.findall('The cat in the hat sat in the flat mat'))

pattern = re.compile(r'First name : (.*) Last name : (.*)')
print(pattern.findall('First name : Ravi Last name : Jiyani'))

serve = "<To serve humans> for dinner >"
pattern = re.compile(r'<(.*?)>')
print(pattern.findall(serve))

prime = "Serve the public trust.\n Protect the innocent.\n Upload the law."
print(prime)
dotStar = re.compile(r'.*')
print(dotStar.search(prime))

dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))
