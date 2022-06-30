'''Unit tests for the rg.algo.toh module

Created on Jun 28, 2022
@author: Rubens Gomes
'''
import unittest
from rg.algo.toh import TowerOfHanoi

class Test(unittest.TestCase):
    """Unit test class to test the TOH functionalities
    """

    def setUp(self):
        """Test fixture to be run to set up state for test cases.
        :param self: refers to any object instance of this type
        """
        self.obj = TowerOfHanoi()

    def test_fail_toh_wrong_input_type(self):
        self.assertRaises(AssertionError, self.obj.toh, 1, 2, 3)

    def test_toh(self):
        """
        :param self: refers to any object instance of this type
        """
        _fromStack = ["0", "1", "2", "3"]
        _toStack = []
        _spareStack = []
        self.assertIsNone(self.obj.toh(_fromStack, _toStack, _spareStack), 'toh failed')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()