helloFile = open(r"D:\Knowledge\Python\git\python-programs\Basics\Files\hello.txt")
print(helloFile.read())
helloFile.close()

helloFile = open(r"D:\Knowledge\Python\git\python-programs\Basics\Files\hello.txt")
print(helloFile.readlines())
helloFile.close()

helloFile = open(r"D:\Knowledge\Python\git\python-programs\Basics\Files\hello.txt", 'a')
helloFile.write('I am good, thanks. \n How are you?')
helloFile.close()