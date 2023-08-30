from json.tool import main
def sumcheck(numberlist,target):
    present=False
    for i in numberlist:
        if target - i in set(numberlist)- {i}:
            present=True
    return present

def main():
    numberlist = [2,3,6,8,1]
    k = 2
    print(sumcheck(numberlist,k))


if __name__ == '__main__':
    main()


