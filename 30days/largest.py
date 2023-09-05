

from array import array
def largest(array):
    large = array[0]
    for i in array:
        large = i if i > large else large
    return large

def main():
    array = [1,3,7,2]
    print(largest(array))

if __name__ == '__main__':
    main()