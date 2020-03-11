import shutil

shutil.copy(r'D:\Knowledge\Python\git\python-programs\Basics\Files\hello.txt',r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder1\TestFolder2')

shutil.copytree(r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder1',r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder3')

shutil.move(r'D:\Knowledge\Python\git\python-programs\Basics\Files\hello.txt', r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder3\New')
