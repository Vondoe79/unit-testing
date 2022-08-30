from gen_function import *

# Single Test cases:

# function call/TEST_1
print('print the square_root 64 is: --> ', int(square_root(64)))  # should produce no Errors

# function call/TEST_2
print('TEST_2 print square_root 64A is: --> ', int(square_root('64A')))  # should produce an Error

# function call with assert statement/TEST_3
assert int(square_root(64)) == 8, 'should be 8 - no Error should be raised'
assert int(square_root(64)) == 7, 'should be 8 - should raise an AssertionError'

breaking_point = 0
