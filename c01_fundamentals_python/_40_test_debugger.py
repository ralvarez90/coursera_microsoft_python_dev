"""
EJEMPLO DE TESTING
"""

import statistics
import unittest


class TestDebugger(unittest.TestCase):

    def setUp(self):
        pass

    def test_string(self):
        self.assertEqual(int('10'), 10)

    def test_mean(self):
        sample_list = [1, 2, 3, 4, 'a', 5]
        sample_list = [x for x in sample_list if type(x) == int]
        self.assertEqual(statistics.mean(sample_list), 3)


if __name__ == '__main__':
    unittest.main()
