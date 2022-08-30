# import
import math
import unittest
from .gen_function import square_root

# Multiple Case using Python In-Built Test Runners to conduct unit testing:---
"""Though a little bit of automation is involved in the "multi_test_case1.py" module in this project, it does not 
provide comprehensive test results of how many cases have failed and how many have passed. We can only manage simple 
cases with this method. Test runners provide a special application for easy execution of test cases and publish a 
clear result of nbr of passed and failed cases. 

Unique features of this test runner are:

Test conditions are coded as methods within a class.
Allows a selfiety of assert methods from unittest library as against a simple assert statement in the earlier examples.

Steps: 1) A class "Testclass" should be created inheriting "Testcase" class from unittest library. 2) Add "self" or a 
parameter (this could be the instance argument "self") as the first argument in all the methods in test functions. 3) 
Replace assert with self.asssert.equal method in Testcase class. 4) Unittest.main() is the entry point. 

"""


# TODO - instead of re-writing this method (square_root), it is imported
# def square_root(l):
#     return math.sqrt(l)


class TestClass(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(square_root(121), 11, "Should be 11")

    def test_case2(self):
        self.assertEqual(square_root(144), 12, "Should be 12")

    def test_case3(self):
        self.assertEqual(square_root(169), 13, "Should be 12")

    def test_case4(self):
        self.assertEqual(square_root(196), 14, "Should be 12")

    def test_case5(self):
        self.assertEqual(square_root(225), 15, "Should be 12")

    def test_case6(self):
        self.assertEqual(square_root(256), 16, "Should be 12")


if __name__ == "__main__":
    unittest.main()

    breaking_point = 0
