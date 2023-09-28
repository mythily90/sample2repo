
def main():
    print("Enter String")
    s=input()
    mid = int(len(s)/2)
    if len(s)%2 == 0:
        mid2 = mid
    else:
        mid2 = mid+1
    if s[:mid] == s[mid2:]:
        print("Symetric")
    else:
        print("not symetric")
    if s[:mid] == s[mid2:][::-1]:
        print("Palindrome")
    else:
        print("not palindrome")

if __name__=="__main__":
    main()