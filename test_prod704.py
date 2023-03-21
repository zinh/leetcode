import unittest
from prod704 import Solution

class TestProd704(unittest.TestCase):
    def test_prod_705(self):
        testcases = [
                {'input': [[-1,0,3,5,9,12], 9], 'expected': 4},
                {'input': [[-1,0,3,5,9,12], 2], 'expected': -1},
                ]
        for idx, testcase in enumerate(testcases):
            solution = Solution()
            actual = solution.search(testcase['input'][0], testcase['input'][1])
            self.assertEqual(testcase['expected'], actual, f'testcase {idx}')
