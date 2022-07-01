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

    def test_power_negative(self):
        self.assertRaises(AssertionError, self.obj.power, 2, -2 )

    def test_power_1(self):
        pairs = [(0,1),(1,1),(2,1),(3,1),(4,1)]
        for i in pairs:
            self.assertTrue(self.obj.power(i[0],i[1])==i[0], f"{i} power failed")

    def test_sqrt_negative(self):
        self.assertRaises(AssertionError, self.obj.sqrt, -1)

    def test_sqrt_numbers(self):
        pairs=[(4,2),(1,1),(16,4),(25,5)]
        for i in pairs:
            self.assertTrue(self.obj.sqrt(i[0])==i[1], f"{i[1]} is not sqrt of {i[0]}")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()