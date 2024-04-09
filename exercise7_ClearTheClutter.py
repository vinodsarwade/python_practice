'''write a program to clear the clutter inside a folder on your computer.
you should use os module to rename all the png images from 1.png all the way till n.
png where n is the number of png files in that folder.do the same for other format.
ex: ndkd.png --> 1.png
    eenr.png --> 2.png
    this.png --> 3.png'''

import os
files = os.listdir("pngFolder")  # take folder
i = 1
for image in files:
    if image.endswith(".png"):  #find images with .png format
        print(image)
        os.rename(f"pngFolder/{image}",f"pngFolder/{i}.png") #rename image 
        i = i + 1  
