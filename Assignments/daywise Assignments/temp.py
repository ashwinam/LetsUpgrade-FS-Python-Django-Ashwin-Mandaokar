import os
os.chdir('C:\\Users\\A_MAN\\Desktop\\mkdir\\New folder')
root_path=os.getcwd()

folderName=['25-05-2021','27-05-2021','29-05-2021','01-06-2021','03-06-2021','08-06-2021','10-06-2021','12-06-2021','15-06-2021']

a='Folder is exist'
print(root_path)
for folder in folderName:
    exitDirectory=os.path.isdir(f'{root_path}/{folder}')
    if exitDirectory==True:
        if 'Folder is exist' in a:
            print('Folder is exist')
            break
    else:
        os.mkdir(f'{root_path}\\{folder}')