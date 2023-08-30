def findlowest(array):
    positiveint = 1
    while True:
        if positiveint in array:
            positiveint=positiveint+1
        else:
            break
    return positiveint
    

def main():
    arraylist=[3, 4,2,5, -1,0,10,1]
    print(findlowest(arraylist))

if __name__=='__main__':
    main()