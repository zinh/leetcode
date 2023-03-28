import unittest
from prod189 import Solution, Solution3


class TestProd189(unittest.TestCase):
    def test_prod_189(self):
        testcases = [
                {"input": [[1,2,3,4,5,6,7], 3], "expected": [5,6,7,1,2,3,4]},
                {"input": [[-1,-100,3,99], 2], "expected": [3,99,-1,-100]},
                ]
        for testcase in testcases:
            solution = Solution()
            output = solution.rotate(testcase['input'][0], testcase['input'][1])
            self.assertEqual(testcase['expected'], output)

    def test_prod_189(self):
        testcases = [
                {"input": [[1,2,3,4,5,6,7], 3], "expected": [5,6,7,1,2,3,4]},
                {"input": [[-1,-100,3,99], 2], "expected": [3,99,-1,-100]},
                ]
        for testcase in testcases:
            solution = Solution3()
            output = solution.rotate(testcase['input'][0], testcase['input'][1])
            self.assertEqual(testcase['expected'], output)
