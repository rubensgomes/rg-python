'''Unit tests for the rg.algo.math module

Created on Jun 28, 2022
@author: Rubens Gomes
'''
import unittest
from rg.algo.math import MathCalc

class Test(unittest.TestCase):
    """A unit test class to test the Math functionalities
    """

    def setUp(self):
        """Test fixture to be run to set up state for test cases.
        :param self: refers to any object instance of this type
        """
        self.obj = MathCalc()

    def test_fail_isprime_wrong_input_type(self):
        self.assertRaises(AssertionError, self.obj.isprime, [])

    def test_fail_isprime_wrong_input(self):
        self.assertRaises(AssertionError, self.obj.isprime, -1)

    def test_isprime_false_0_1(self):
        non_primes = [0,1]
        for i in non_primes:
            self.assertFalse(self.obj.isprime(i), f"{i} is prime")

    def test_isprime_true(self):
        primes = [2,3,5,7,11,13,17]
        for i in primes:
            self.assertTrue(self.obj.isprime(i), f"{i} is not prime")

    def test_isprime_false(self):
        primes = [4,6,8,9,10,12]
        for i in primes:
            self.assertFalse(self.obj.isprime(i), f"{i} is prime")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()