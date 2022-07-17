'''Unit tests for the rg.algo.edit_dist module
Created on Jul 16, 2022

@author: 816461
'''
import unittest
from rg.algo.edit_dist import edit_dist

class Test(unittest.TestCase):
    """A unit test class to test the edit_dist functionalities
    """

    def setUp(self):
        """Test fixture to be run to set up state for test cases.
        :param self: refers to any object instance of this type
        """

    def test_simple_strings(self):
        s = 'a cat'
        t = 'the cats'
        result = edit_dist(s, t)
        self.assertTrue(result == 4, "result is not correct")

if __name__ == "__main__":
    unittest.main()