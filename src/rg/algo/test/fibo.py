'''Unit tests for the rg.algo.fibo module

Created on Jun 26, 2022
@author: Rubens Gomes
'''
import unittest
from rg.algo.fibo import FiboCalc


class Test(unittest.TestCase):
    """A unit test class to test the FiboCalc functionalities
    """

    def setUp(self):
        """Test fixture to create an object instance of the FiboCalc type.
        :param self: refers to any object instance of this type
        """
        unittest.TestCase.setUp(self)
        self.obj = FiboCalc()

    def test_fail_fibo_wrong_input_type(self):
        self.assertRaises(AssertionError, self.obj.fibo, [])

    def test_fail_fibo_negative_input(self):
        self.assertRaises(AssertionError, self.obj.fibo, -1)

    def test_fail_fibodp_negative_input(self):
        self.assertRaises(AssertionError, self.obj.fibo_dp, -1)

    def test_fibo_5(self):
        self.assertTrue(self.obj.fibo(5) == 5, "fibo of 5 is NOT 5")

    def test_fibodp_5(self):
        self.assertTrue(self.obj.fibo_dp(5) == 5, "fibo_dp of 5 is NOT 5")

if __name__ == "__main__":
    # import sys;sys.argv = ["", "FiboTest.failDueToNegativeInput"]
    unittest.main()
