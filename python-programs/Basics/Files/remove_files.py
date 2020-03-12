import os
import shutil
import send2trash

#os.unlink(r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder3\New')
#os.removedirs(r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder3')
#shutil.rmtree(r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder3')

send2trash.send2trash(r'D:\Knowledge\Python\git\python-programs\Basics\Files\TestFolder3')

for folder_name, sub_folders, file_names in os.walk(r'D:\Knowledge\Python\git\python-programs\Basics\Files'):
    print('Folder Name : '+folder_name)
    print('Sub Folders : '+str(sub_folders))
    print('Files : '+str(file_names))