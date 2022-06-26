"""This module provides an abstraction to calculate Fibonacci numbers.

Fibonacci formula is fibo_obj(n) = fibo_obj(n-1) + fibo_obj(n-2).
Sample Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, ....

Created on Jun 25, 2022
@author: Rubens Gomes
"""
import time
from pickle import NONE

class FiboCalc(object):
    """A type that provides functionalities to calculate Fibonacci numbers
    """

    # _memo is a dictionary class variable used to store previously calculated Fibonacci numbers.
    _memo = {}

    def __init__(self):
        """Constructor to initialize an object instance of this type
        :param self: refers to any object instance of this type
        """

    @staticmethod
    def get_memo():
        """Returns the value of the class variable _memo containing previously stored fibonacci numbers

        Keyword arguments:
        :param self: refers to any object instance of this type
        """
        return FiboCalc._memo

    def __str__(self):
        """Returns a stringfied version of this object to print an object of this type.

        Keyword arguments:
        :param self: refers to any object instance of this type
        """
        return "_memo list: " + str(FiboCalc._memo)

    def fibo(self, n):
        """Returns the Fibonacci number for the given index n
        
        It uses the common solution of recursion function with no optimization;
        that is, no dynamic programming is involved in the solution.
 
        Keyword arguments:
        :param n -- a positive integer number to represent the index of of the fibonacci
        number to be calculated; for example, obj(3) is 2, where index n is 3
        """

        FiboCalc._check_input(n)

        if n <= 2:
            ans = 1
        else:
            ans = self.fibo(n - 1) + self.fibo(n - 2)

        return ans


    def fibo_dp(self, n):
        """Returns the Fibonacci number for the given index n
        
        It uses a dynamic programming technique with memorization to optimize the 
        calculation of Fibonacci number. 
 
        Keyword arguments:
        :param n -- a positive integer number to represent the index of of the Fibonacci
        number to be calculated; for example, fibo_dp(3) is 2, where index n is 3
        """

        FiboCalc._check_input(n)

        if n in FiboCalc._memo: 
            return FiboCalc._memo[n]
        elif n <= 2:
            ans = 1
        else:
            ans = self.fibo_dp(n - 1) + self.fibo_dp(n - 2)

        # store ans to be used in future Fibonacci calculations (DP - Dynamic Programming)
        FiboCalc._memo[n] = ans
        return ans

    @staticmethod
    def _check_input(n):
        # simple static method to validate method precondition input
        assert n > 0, 'n must be greater than zero'
        return None

if __name__ == '__main__':
    NS_TO_MS_FACTOR=0.000001
    # obj is an object used to test the different Fibonacci calculator methods
    obj = FiboCalc()
    # notice that 35 takes 
    N = [5, 10, 20, 30]

    for n in N:
        print(f"Fibonacci index n is:  {n}")

        tic = time.perf_counter_ns()
        ans = obj.fibo(n)
        toc = time.perf_counter_ns()
        elapsed_ms = (toc - tic) * NS_TO_MS_FACTOR
        print(f"fibo    ans: {ans} / elapsed: {elapsed_ms:.4f} ms")

        tic_dp = time.perf_counter_ns()
        ans = obj.fibo_dp(n)
        toc_dp = time.perf_counter_ns()
        elapsed_dp_ms = (toc_dp - tic_dp) * NS_TO_MS_FACTOR
        print(f"fibo_dp ans: {ans} / elapsed: {elapsed_dp_ms:.4f} ms")
        print(f"fibo_dp is  {(elapsed_ms / elapsed_dp_ms):.2f} times faster than obj")
        print(obj)
