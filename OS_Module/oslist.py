import os
folders = os.listdir("data")  # it will display all the present folders in data
print(folders)

for folder in folders: # print all the folders in column
    print(folder)

for folder in folders:
    print(os.listdir(f"data/{folder}")) # i have made another file in tutorial 10 ,it will display that file also 