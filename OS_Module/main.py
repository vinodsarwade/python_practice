import os
if(not os.path.exists("data")): #if i didnt write this it will create error for data file already exist so we have written it in if condition.
    os.mkdir("data")    #it will create a directory named data


for i in range (0, 100):
    os.mkdir(f"data/day{i+1}")  #this loop traverse up to 100 and print day from 0 - 100

