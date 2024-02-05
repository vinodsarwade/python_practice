import os
for i in range (0, 100):
    os.rename(f"data/data{i+1}", f"data/tutorial{i + 1}")  #it will rename all the folders in data file from day to tutorial