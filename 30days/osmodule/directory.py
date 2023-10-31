
import os

#GETCWD. The folder where the Python script is running is known as the Current Directory. This is not the path where the Python script is located.

def current_path():
    print("Current working directory before")
    print(os.getcwd())


#Change current Working directory
def changepath():
    current_path()
    os.chdir("../")
    current_path()

#Madke directory with mode. os.mkdir can be vacalled with path alone, without mode
def makedir():
    dir = "testdir"
    parentdir = "/home/mythily/Repository/python-sample/30days/osmodule/"
    # ospath = os.path.join(parentdir,dir)
    # print(ospath)
    # mode = 0o666
    # os.mkdir(ospath,0o777)
    path2 = os.path.join(parentdir, "c")
    os.makedirs(path2)



#list directory contents
def listdir():
    path=os.path.join("/home/mythily","")
    print(os.listdir(path))



if __name__ == "__main__":
    #makedir()
    listdir()