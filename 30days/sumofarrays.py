from array import array


def sumofarray(numarray):
    sum = 0
    for i in numarray:
        sum=sum+i
    return sum

def main():
    array=[1, 2, 3]
    print( sumofarray(array))

if __name__ == '__main__':
    main()