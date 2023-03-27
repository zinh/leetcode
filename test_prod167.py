import unittest
from prod167 import Solution, Solution2


class TestProd189(unittest.TestCase):
    def test_prod_189(self):
        testcases = [
                {"input": [[2,7,11,15], 9], "expected": [1, 2]},
                {"input": [[2, 3, 4], 6], "expected": [1, 3]},
                {"input": [[5, 25, 75], 100], "expected": [2, 3]},
                {"input": [[1,2,3,4,4,9,56,90], 8], "expected": [4, 5]},
                ]
        for testcase in testcases:
            solution = Solution()
            output = solution.twoSum(testcase['input'][0], testcase['input'][1])
            self.assertEqual(testcase['expected'], output)

    def test_prod_189_2(self):
        testcases = [
                {"input": [[2,7,11,15], 9], "expected": [1, 2]},
                {"input": [[2, 3, 4], 6], "expected": [1, 3]},
                {"input": [[5, 25, 75], 100], "expected": [2, 3]},
                {"input": [[1,2,3,4,4,9,56,90], 8], "expected": [4, 5]},
                ]
        for testcase in testcases:
            solution = Solution2()
            output = solution.twoSum(testcase['input'][0], testcase['input'][1])
            self.assertEqual(testcase['expected'], output)
