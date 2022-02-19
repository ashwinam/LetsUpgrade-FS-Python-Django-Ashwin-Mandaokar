'''
Requirements
1. whenever user run this script along with, user can give two arguments like a two folder name
    i. first folder include jpg files 
    ii. second folder automatically created with the png files
'''
import sys
import os
from PIL import Image


# using sys module grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check second folder exist, if not then create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through entire first folder, convert jpg to png and save to the new folder.
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    cleaned_name = os.path.splitext(filename)[0]
    # img.save(f"{output_folder}{filename}.png", "png") # this create problem it creates a name.jpg.png, need to clean the name
    img.save(f"{output_folder}{cleaned_name}.png", "png")
    print("All Done !")
