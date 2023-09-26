
from math import sqrt




# check whether number is amstong number
def amstrong(n):
    sum=0
    order=len(str(n))
    for i in str(n):
        sum=sum+(int(i) ** order)
    if sum == n:
        return True
    else:
        return False

#check whether number is prime
def isprime(n):
    if n == 0 or n == 1:
            return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

#get prime numbers within a range
def primenumberinrange(a,b):
    for j in range(a,b):
        if isprime(j):
            print(j)


def arrayrot(array,k):
    #n=len(array)
    print(array[k:]+array[:k])


#swap first and last element of array
def swapelement(array):
    n=len(array)
    print(array[-1:]+array[1:-1]+array[:1])

if __name__=='__main__':
    #i = 1531
    #print(amstrong(i))
    #primenumberinrange(0,100)
    arr=[ i for i in range(10,20)]
    #arrayrot(arr,3)
    swapelement(arr)
