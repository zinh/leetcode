import unittest
from prod733 import Solution

class TestProd733(unittest.TestCase):
    def test_prod_733(self):
        testcases = [
                {'input': [[[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2], 'expected': [[2,2,2],[2,2,0],[2,0,1]]},
                ]
        for idx, testcase in enumerate(testcases):
            inp = testcase['input']
            solution = Solution()
            actual = solution.floodFill(inp[0], inp[1], inp[2], inp[3])
            self.assertEqual(testcase['expected'], actual, f'testcase {idx + 1}')
