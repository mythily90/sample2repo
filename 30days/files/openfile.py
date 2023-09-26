'''Since relative path is provided 
make sure you cd to current working dir in terminal 
before running the program else you might get filenot found 
'''
# with open method
def openfile (filename):
    with open(filename,'r') as file:
        for line in file:
            for word in line.split():
                print(word)

#count number of lines
def countlines(filename):
    count = 0
    file2 = open(filename)
    print(type(file2))
    for line in file2:
        count = count+1
    return count

if __name__=='__main__':
    print(countlines('filename1.txt'))