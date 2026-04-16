"""
EJEMPLO DE TESTING
"""

import statistics
import unittest


class TestDebugger(unittest.TestCase):

    def setUp(self):
        pass

    def testString(self):
        self.assertEqual(int('10'), 10)

    def testMean(self):
        sampleList = [1, 2, 3, 4, 'a', 5]
        sampleList = [x for x in sampleList if type(x) == int]
        self.assertEqual(statistics.mean(sampleList), 3)


if __name__ == '__main__':
    unittest.main()
