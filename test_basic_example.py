import unittest

from pract_venv.basic_example import full_name


class MyTestCase(unittest.TestCase):
    def test_basic_example(self):
        actual = full_name()
        expected = 'Kofi Doe'
        self.assertEqual(actual, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
