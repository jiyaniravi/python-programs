from io import StringIO
# https://docs.python.org/3.0/whatsnew/3.0.html
# https://stackoverflow.com/questions/11914472/stringio-in-python3

message = "This is just a normal string !"

f = StringIO(message)
print(f.read())

f.write('Added this extra text !')
f.seek(0)
print(f.read())