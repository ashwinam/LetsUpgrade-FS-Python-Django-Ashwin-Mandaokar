import csv
import os
from db_ops import bulk_insertion

list_file = [file for file in os.listdir() if file.endswith("csv")]

print("Index \t File")

for i,each in enumerate(list_file):
    print(i, "\t",each)

ch = int(input("Enter the index :"))

file_name = list_file[ch]

with open (file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    data = [each for each in csv_reader]

print(data)
bulk_insertion(data,"activity")