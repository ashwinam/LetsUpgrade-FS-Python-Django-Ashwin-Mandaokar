from db_ops import download
import csv

data = download("activity")

new_file_name = "download.csv"

with open(new_file_name, 'w', newline = '') as file:
	writer = csv.writer(file)
	writer.writerows(data)

print("task completed")
