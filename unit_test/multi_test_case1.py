from gen_function import *


# multiple test cases using assert statement:---
def unittest_1():
    assert square_root(64) == 8, 'should be 8'
    assert square_root(81) == 9, 'should be 9'
    assert square_root(100) == 10, 'should be 10'


if __name__ == '__main__':
    unittest_1()
    print('Everything Passed test')

    breaking_point = 0
