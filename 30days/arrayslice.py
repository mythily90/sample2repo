#rotate array be k position
def arrayrot(array,k):
    #n=len(array)
    print(array[k:]+array[:k])


#swap first and last element of array
def swapelement(array):
    n=len(array)
    print(array[-1:]+array[1:-1]+array[:1])

if __name__ == '__main__':
    arr=[ i for i in range(10,20)]
    #arrayrot(arr,3)
    swapelement(arr)