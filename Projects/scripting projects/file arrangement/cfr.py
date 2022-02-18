# automate the file arrangement system
# file system link  C:\Users\A_MAN\Downloads

'''
Requirements:-
1) access the place where the file system will be applicable 
2) make a folders if there is no folders in there
	-check the folders name if there in there then dont make one, if not then make one
3) access the files using extension
	- files send it to the designated folders
Improvements:-
1) make a dynamic if statements.
2) recursive way for folders if folder includes movie then folder directly move


'''
import os
import shutil

def list_out_files():

	files = os.listdir("C:\\Users\\A_MAN\\Downloads")
	for file in range(len(files)):
		print(file,files[file])

def	making_directories():

	list_of_directories = ['Images','Compressed','video','Documents','Music','Programs']
	current_directory = os.getcwd()
	for folder in list_of_directories:
		is_folder_exist = os.path.isdir(f'{current_directory}/{folder}')
		if is_folder_exist:
			continue
		else:
			os.mkdir(f'{current_directory}/{folder}')	
			
def	arranging_files():
	files = os.listdir("C:\\Users\\A_MAN\\Downloads")


	for file in range(len(files)):
		if os.path.isfile(files[file]) and files[file].endswith('jpg') or files[file].endswith('png') or files[file].endswith('gif') or files[file].endswith('jpeg'):
			shutil.move(src=(f"C:\\Users\\A_MAN\\Downloads\\{files[file]}"), dst=("C:\\Users\\A_MAN\\Downloads\\Images\\"))
			print('images done')

		if files[file].endswith('pdf') or files[file].endswith('docx') or files[file].endswith('doc') or files[file].endswith('pptx') or files[file].endswith('ppt') or files[file].endswith('xls') or files[file].endswith('csv') or files[file].endswith('xlsx'): 
			shutil.move(src=(f"C:\\Users\\A_MAN\\Downloads\\{files[file]}"), dst=("C:\\Users\\A_MAN\\Downloads\\Documents\\"))

		if files[file].endswith('zip') or files[file].endswith('rar'):
			shutil.move(src=(f"C:\\Users\\A_MAN\\Downloads\\{files[file]}"), dst=("C:\\Users\\A_MAN\\Downloads\\Compressed\\"))



if __name__ == "__main__":
	# setup the directory
	os.chdir("C:\\Users\\A_MAN\\Downloads") 

	list_out_files()

	making_directories()

	arranging_files()


