"""Module of math related functions.

Created on Jun 28, 2022
@author: Rubens Gomes
"""
from math import sqrt


class MathCalc(object):
    """A class that solves the Math problem
    """

    def __init__(self):
        """Constructor to initialize an object instance of this type
        :param self: refers to any object instance of this type
        """

    def isprime(self, n):
        """Returns true if n is prime; false, otherwise.
    
        :param n: a positive integer number
        """

        MathCalc._check_isprime_input(n)

        if(n == 0 or n == 1):
            return False

        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False

        return True

    def power(self, a, b):
        """Returns the power of a to b
        :param a:  an integer number
        :param b: a positive integer number
        """

        assert isinstance(a, int), "a must be integer"
        assert isinstance(b, int), "b must be integer"
        assert b>0, "b must be positive"

        if b==1: return a

        return a*self.power(a, b-1)

    def sqrt(self, n):
        """Returns the square root of n using bi-section brute force guesses
        :param n: a positive integer number
        """

        assert isinstance(n, int), "n must be integer"
        assert n>0, "n must be positive"

        return MathCalc._sqrt(n, 1, n)

    @staticmethod
    def _sqrt(n, low, high):
        if(n==0): return 0
        if(n==1): return 1

        if(high<low): raise ValueError(f"cannot determine sqrt of {n}")

        guess = int((high+low)/2)
        num=guess*guess

        if num==n:
            return guess
        elif num>n: 
            return MathCalc._sqrt(n, low, guess-1)
        else: 
            return MathCalc._sqrt(n,guess+1, high)

    @staticmethod
    def _check_isprime_input(n):
        # simple static method to validate method precondition input
        assert isinstance(n, int), "n must be an integer"
        assert n >= 0, "n must be positive"
        return None
