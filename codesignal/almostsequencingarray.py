'''
Given a sequence of integers as an array, 
Determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

    For sequence = [1, 3, 2, 1], the output should be
    solution(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    solution(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

'''


def first_bad_pair(s):
    lens=len(s)
    for i in range (0,lens-1):
        if s[i] >= s[i+1]:
            return i
    return -1


def solution(sequence):
    if len(sequence) == 2:
        return True
    seqe=sequence
    j = first_bad_pair(seqe)
    if j == -1:
        return True
    if j == len(seqe) - 1:
        return True
    if j == len (seqe) - 2:
            return True
    if first_bad_pair(seqe[j-1:j]+seqe[j+1:]) == -1:
        return True
    if first_bad_pair(seqe[j:j+1]+seqe[j+2:]) == -1:
        return True
    return False     


if __name__=="__main__":
    seq=[123, -17, -5, 1, 2, 3, 12, 43, 45]
    #seq = [0, -2, 5, 6]
    #seq = [1,2,1,2]
    ans=solution(seq)
    print(ans)