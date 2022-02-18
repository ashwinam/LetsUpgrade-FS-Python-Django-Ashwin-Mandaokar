# ---------Finder Project---------

'''what do finder project do?
ans :- finder project helps to find a particular file with the location.

Requirements:-
1) get drives function for all the drives available in system/pc.
2) scanner function do the scan the all drives , on there folders and files in a recursive way and
save it on a dictionery 
3) pickle module help save the dictionery as a binery file ,so for that need a save function and open 
function for accessing the dictionery
4)ask the user file name for searching.
	- use regex for searching the keyword and match with the dictionery keys and give the that keys values
'''

import os
import pickle
import time
import re

t1 = time.time()


def get_drives():
	temp = []
	list_of_drives = []
	drives = os.popen("wmic logicaldisk get caption")

	for drive in drives.readlines():
		temp.append(drive.strip())

	for each_drive in temp:
		if each_drive:
			list_of_drives.append(each_drive)
	return list_of_drives[1:]

def save_index(index):
	fr = open("finder_index.index", "wb")
	pickle.dump(index,fr)
	fr.close()

def open_index():
	fr = open("finder_index.index", "rb")
	index = pickle.load(fr)
	return index

def scanner():
	i = 0
	index = {}
	list_of_drives = get_drives()
	print("Creating Index...")
	for drive in list_of_drives:
		resp = os.walk(drive)
		for root,dirs,files in resp:
			for file in files:
				file_path = root + "\\" + file
				if file in index:
					file = file + "|" + str(i)
					i = i + 1
				index[file] = file_path
	save_index(index)
	print("data completed")

def searching_files():
	index = open_index()
	pattern = input(r"Please enter the file name : ")

	k = 1
	for i,j in index.items():
		match = re.search(pattern,i,re.I)
		if match:
			print(k,"\t", j)
			print("-"*125	)
			k = k + 1

if __name__ == '__main__':

	print("Welcome To the Finder".center(115,'='))
	# scanner()
	# index = open_index()
	# for i,j in index.items():
	# 	print(i ,"\t", j)
	while True:
		print('''
			Please Choose between 1 & 2
			1.Update the index
			2.Searching the file
			3.Exit
			''')
		user_choice = int(input("Enter your choice: "))
		if user_choice == 1:
			scanner()
		elif user_choice == 2:
			searching_files()
		elif user_choice == 3:
			break
	t2 = time.time()
	print("time taken...", t2-t1)




