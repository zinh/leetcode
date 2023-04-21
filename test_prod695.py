import unittest
from prod695 import Solution

class Test695(unittest.TestCase):
    def test_695(self):
        testcases = [
                {'input': [[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]], 'expected': 6},
                {'input': [[[0,0,0,0,0,0,0,0]]], 'expected': 0},
                {'input': [[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]], 'expected': 4},
                ]
        for idx, testcase in enumerate(testcases):
            inp = testcase['input']
            solution = Solution()
            actual = solution.maxAreaOfIsland(inp[0])
            self.assertEqual(testcase['expected'], actual, f'testcase {idx + 1}')
