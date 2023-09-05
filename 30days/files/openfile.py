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

#just open
def openfile2(filename):
    file2 = open(filename)
    for line in file2:
        print(line)

if __name__=='__main__':
    openfile2('filename1.txt')