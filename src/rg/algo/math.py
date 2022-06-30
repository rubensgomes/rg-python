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


    @staticmethod
    def _check_isprime_input(n):
        # simple static method to validate method precondition input
        assert isinstance(n, int), "n must be an integer"
        assert n >= 0, "n must be positive"
        return None
