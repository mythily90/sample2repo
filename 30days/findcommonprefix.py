def findcommon(sts):
    min = sts[0]
    k = 1
    while True:
        passover=False
        for i in sts:
            if min[:k] != i[:k]:
                passover=True
                break
        if not passover:
            k = k+1
        else:
            print(min[:k-1])
            break


if __name__ == "__main__":
    arr=["flower","flow","flight"]
    findcommon(arr)