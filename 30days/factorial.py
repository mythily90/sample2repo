from functools import reduce
from operator import add

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)



if __name__ == '__main__':
    #print(sum.__doc__)
    #print(sum([1,2,3]))
    # arr=[3,4,6,5,7]
    # val=reduce(lambda a,b: a+b ,arr)
    # print(val)
    print(fact(5))