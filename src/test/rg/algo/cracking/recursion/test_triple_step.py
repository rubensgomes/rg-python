'''
Created on Jul 11, 2022

@author: 816461
'''
import unittest

from rg.algo.cracking.recursion.triple_step import TripleStep


class Test(unittest.TestCase):
    """A unit test class to test the TripleStep functionalities
    """

    def setUp(self):
        """Test fixture to create an object instance of the TripleStep type.
        :param self: refers to any object instance of this type
        """
        unittest.TestCase.setUp(self)
        self.obj = TripleStep()

    def test_for_3_step_stairs(self):
        self.assertTrue(self.obj.triple_step(3) == 4, "triple steps of 3 step-stairs is not 4")

    def test_for_4_step_stairs(self):
        self.assertTrue(self.obj.triple_step(4) == 7, "triple steps of 4 step-stairs is not 7")

    def test_for_3_step_stairs_DP(self):
        self.assertTrue(self.obj.triple_step_dp(3) == 4, "triple steps of 3 step-stairs is not 4")

    def test_for_4_step_stairs_DP(self):
        self.assertTrue(self.obj.triple_step_dp(4) == 7, "triple steps of 4 step-stairs is not 7")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
