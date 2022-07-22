'''Addresses the following problem:
1. Find a pair with the given sum in an array:
Given an unsorted integer array, find a pair with the given sum in it.

Created on Jul 17, 2022

@author: 816461
'''


def find_pair(A, s):
    """Returns a set of tuples of elements in array A whose sum add up to 
    given value of s. This is a brute force solution with O(n^2)

    - A: an array of integers
    - s: a given sum
    """
    S = set()
    i = 0

    for a in A:
        i += 1
        for b in A[i:]:
            if (a + b) == s:
                t = (a, b)
                print(t)
                S.add(t)

    return S

def find_pair_opt(A, s):
    """Returns a set of tuples of elements in array A whose sum add up to 
    given value of s. This is an optimal solution with O(n^2)

    - A: an array of integers
    - s: a given sum
    """
    S = set()
    i = 0

    for a in A:
        i += 1
        for b in A[i:]:
            if (a + b) == s:
                t = (a, b)
                print(t)
                S.add(t)


    return S


if __name__ == "__main__":
    # array A = [ 1, 2 ]
    # set S = set() or S = {1, 2}
    # dict D = {}
    # tupple T = ( 1, 2 )
    A = [ 1, 3, 2, 3, 4, 5, -1, 2, 3 ]
    s = 4
    print(f"A {A} / sum {s}")
    ans = find_pair(A, s)
    print(f"Answer: array: {A} / sum: {s} / ans: {ans}")

