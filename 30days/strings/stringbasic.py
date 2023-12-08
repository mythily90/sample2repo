# Remove Letters From a String in Python

def removeletter(s,e):
    print(s)
    new=s.replace(e,'')
    print(new)



if __name__ == "__main__":
    s="geeksforgeeks"
    removeletter(s,'g')