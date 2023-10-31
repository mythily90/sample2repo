#Write a Python program to list only directories, files and all directories, files in a specified path. 
import os

path="/home/mythily/Repository/python-sample/"

for content in os.listdir(path):
    print(content)
    if os.path.isdir(os.path.join(path,content)):
        print("is directory")
    else:
        print("File")