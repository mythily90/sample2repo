#find Second largest element

def second_largest(ar):
    secarr = [x for x in ar if x< max(arr)]
    return max(secarr)

# find n largest elements
def n_largest2(ar, N):
    newar=[]
    ar2=ar
    for i in range(0,N):
        newar.append(max(ar2))
        ar2 = [x for x in ar2 if x < max(ar2)]
    return newar

# return even nos from list
def eve_num(ar):
    evar = [x for x in ar if x%2 == 0]
    return evar


# remove empty list from list using join
def remov_empty(arr):
    print(arr)
    #s = [x for x in arr if x!=[]]
    l=len(arr)
    x = list(map(str,arr))
    y = "".join(x)
    y=y.replace("[]",'')
    y=list(map(int,y))
    return y

# remove empty list with enumeration:
def remove_emtu(arr):
    s=[ele for i,ele in enumerate(arr) if ele !=[]]   
    return s   

def listtest(arr):
    ar1=arr[:]
    ar1.pop(1)
    print(ar1)
    print(arr)

def countocurrnce(arr,ele):
   print(arr.count(ele))


def listcomp(arr,ele):
    oc = {item: arr.count(item) for item in arr}
    print(oc)


#remove empty tuples
def empty_tup(tup):
    # s=filter(None,tup)
    # return list(s)
    s = [i for i in tup if i != ()]
    return(s)

def duplicates_list(li):
    oc = {item: lis.count(item) for item in li}
    k = [i for i in oc if oc[i] > 1 ]
    print(k)

#find cummilative sum
def cumilative_sum(li):
    s =[]
    s.append( li[0])
    for i in range(1,len(li)):
       s.append(li[i]+s[i-1])
    print(s)

# Sum digits of each element in array
def digit_sum(num):
    sum = 0
    while num>0:
        sum = sum+num%10
        num = int(num/10)
    return sum
def sum_arr(arr):
    s = [digit_sum(i) for i in arr]
    print(s)


#break into chunks
def breakchunks(arr,n):
    sar=[]
    bar=[]
    i=0
    while i != len(arr):
        print(i)
        print(bar)
        print(sar)
        i = i+1
        if i%n == 0:
            sar.append(arr[i-1])
            bar.append(sar)
            sar = []
        else:
            sar.append(arr[i-1])
        
    bar.append(sar)
    bar=list(filter(None,bar))
    print(bar)

def sortusinganotherarr(l1,l2):
    a = sorted(list(set(l2)))
    slist=[]
    for i in a:
        for j in range(0,len(l2)):
            if i == l2[j]:
                slist.append(l1[j])

    print(slist)
        

if __name__ == '__main__':
    arr = [1,3,7,8,3,7,3]
    #print(second_largest(arr))
    #print(n_largest2(arr,3))
    #print(eve_num(arr))
    #arr2 = [5,6,[],3,[],[],9]
    #print(remov_empty(arr2))
    #print(remove_emtu(arr2))
    #listtest(arr)
    lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
    #countocurrnce(arr,7)
    ar3=[12, 67, 98, 34]
    sum_arr(ar3)
    #listcomp(lis,'a')
    # tup =  [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),() ]
    # print(empty_tup(tup))
    # duplicates_list(lis)
    #l=[10, 20, 30, 40, 50]
    #cumilative_sum(l)
    # ar=['geeks', 'for', 'geeks', 'like', 
    #        'geeky','nerdy', 'geek', 'love', 
    #            'questions','words', 'life','ok'] 
    # breakchunks(ar,4)
    a1=  ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    a2= [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
    sortusinganotherarr(a1,a2)
