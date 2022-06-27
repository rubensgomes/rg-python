"""This module provides a recursive solution to the Tower of Hanoi problem

Created on Jun 26, 2022
@author: Rubens Gomes
"""


def toh(fromStack, toStack, spareStack):
    """Demonstrates how to solve Tower of Hanoi problem using recursion

    :param fromStack: array containing the n disks to be moved from
    :param toStack: empty array to where disks should be moved to
    :param spareStack: empty array to keep temporary spare disks during moves

    Returns None
    """

    assert len(fromStack) != 0, 'fromStack is empty'
    assert len(toStack) == 0, 'toStack should be empty'
    assert len(spareStack) == 0, 'spareStack should be empty'

    print("-------")
    print ("initial fromStack: ", fromStack)
    print ("initial toStack: ", toStack)
    print ("initial spareStack: ", spareStack)
    print("-------")

    # delegate computation to recursive function
    _toh(len(fromStack), fromStack, toStack, spareStack)

    print("-----------------------")
    print ("final fromStack: ", fromStack)
    print ("final toStack: ", toStack)
    print ("final spareStack: ", spareStack)
    print("-----------------------")

    return None


def _toh(n, fromStack, toStack, spareStack):

    # sanity check
    assert n > 0, 'n actual parameter value is invalid'

    # recursive base case
    if n == 1:
        toStack.append(fromStack.pop())
        print ("fromStack: ", fromStack)
        print ("toStack: ", toStack)
        print ("spareStack: ", spareStack)
        print("-------")
        return None

    # notice these are recursive calls
    _toh(n - 1, fromStack, spareStack, toStack)
    _toh(1, fromStack, toStack, spareStack)
    _toh(n - 1, spareStack, toStack, fromStack)
    return None


if __name__ == '__main__':
    print('toh starting...')
    _fromStack = ["0", "1", "2", "3"]
    _toStack = []
    _spareStack = []

    print ("initial fromStack: ", _fromStack)
    print ("initial toStack: ", _toStack)
    print ("initial spareStack: ", _spareStack)
    print("-------")

    toh(_fromStack, _toStack, _spareStack)

    print ("final fromStack: ", _fromStack)
    print ("final toStack: ", _toStack)
    print ("final spareStack: ", _spareStack)
