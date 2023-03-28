import unittest
from prod977 import Solution

class TestProd977(unittest.TestCase):
    def test_prod_977(self):
        testcases = [
                {'input': [[-4,-1,0,3,10]], 'expected': [0,1,9,16,100]},
                {'input': [[-7,-3,2,3,11]], 'expected': [4,9,9,49,121]},
                {'input': [[1]], 'expected': [1]},
                {'input': [[-1]], 'expected': [1]},
                {'input': [[-1, 10]], 'expected': [1, 100]},
                ]
        for idx, testcase in enumerate(testcases):
            solution = Solution()
            actual = solution.sortedSquares(testcase['input'][0])
            self.assertEqual(testcase['expected'], actual, f'testcase {idx}')
