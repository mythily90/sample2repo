'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

    For inputString = "(bar)", the output should be
    solution(inputString) = "rab";
    For inputString = "foo(bar)baz", the output should be
    solution(inputString) = "foorabbaz";
    For inputString = "foo(bar)baz(blim)", the output should be
    solution(inputString) = "foorabbazmilb";
    For inputString = "foo(bar(baz))blim", the output should be
    solution(inputString) = "foobazrabblim".
    Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

'''

def solution(inputString):
    a = inputString
    k = list(a)
    stackindex=[]
    newarr=[]
    total = 0
    for i in range (0, len(inputString)):
        if a[i]=='(':
            totalstackelements=total+len(stackindex)
            stackindex.append(i-totalstackelements)
            #stackindex.append(i)
        elif a[i] == ')':
            ind=stackindex.pop()
            total=total+2
            newarr=newarr[:ind]+newarr[ind:][::-1]
        else:
            newarr.append(a[i])
    return "".join(newarr)