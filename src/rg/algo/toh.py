"""This module provides a recursive solution to the Tower of Hanoi problem

Created on Jun 26, 2022
@author: Rubens Gomes
"""
from array import array

DEBUG=False

class TowerOfHanoi(object):
    """A class that solves the tower of hanoi problem
    """

    def __init__(self):
        """Constructor to initialize an object instance of this type
        :param self: refers to any object instance of this type
        """

    def toh(self, fromStack, toStack, spareStack):
        """Demonstrates how to solve Tower of Hanoi problem using recursion

        :param fromStack: array containing the n disks to be moved from
        :param toStack: empty array to where disks should be moved to
        :param spareStack: empty array to keep temporary spare disks during moves

        Returns None
        """

        TowerOfHanoi._check_inputs(fromStack, toStack, spareStack)
        # delegate computation to recursive function
        self._toh(len(fromStack), fromStack, toStack, spareStack)

        return None


    def _toh(self, n, fromStack, toStack, spareStack):

        # sanity check
        assert n > 0, "n actual parameter value is invalid"

        # recursive base case
        if n == 1:
            toStack.append(fromStack.pop())

            if DEBUG:
                print ("fromStack: ", fromStack)
                print ("toStack: ", toStack)
                print ("spareStack: ", spareStack)
                print("-------")

            return None

        # notice these are recursive calls
        self._toh(n - 1, fromStack, spareStack, toStack)
        self._toh(1, fromStack, toStack, spareStack)
        self._toh(n - 1, spareStack, toStack, fromStack)

        return None

    @staticmethod
    def _check_inputs(fromStack, toStack, spareStack):
        """Ensure that the passed in actual parameters are valid.

        :param fromStack: array containing the n disks to be moved from
        :param toStack: empty array to where disks should be moved to
        :param spareStack: empty array to keep temporary spare disks during moves

        Returns None
        """
        assert isinstance(fromStack, array), "fromStack is not an array"
        assert isinstance(toStack, array), "toStack is not an array"
        assert isinstance(spareStack, array), "spareStack is not an array"

        assert len(fromStack) != 0, "fromStack is empty"
        assert len(toStack) == 0, "toStack should be empty"
        assert len(spareStack) == 0, "spareStack should be empty"

        return None

if __name__ == "__main__":
    toh = TowerOfHanoi()
    print("toh starting...")
    _fromStack = ["0", "1", "2", "3"]
    _toStack = []
    _spareStack = []

    print ("initial fromStack: ", _fromStack)
    print ("initial toStack: ", _toStack)
    print ("initial spareStack: ", _spareStack)
    print("-------")

    toh.toh(_fromStack, _toStack, _spareStack)

    print ("final fromStack: ", _fromStack)
    print ("final toStack: ", _toStack)
    print ("final spareStack: ", _spareStack)
