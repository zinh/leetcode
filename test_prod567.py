import unittest
from prod567 import Solution

class TestProd19(unittest.TestCase):
    def test_prod_19(self):
        testcases = [
                {'input': ["ab", "eidbaooo"], 'expected': True},
                {'input': ["ab", "eidboaoo"], 'expected': False},
                ]
        for idx, testcase in enumerate(testcases):
            inp = testcase['input']
            solution = Solution()
            actual = solution.checkInclusion(inp[0], inp[1])
            self.assertEqual(testcase['expected'], actual, f'testcase {idx + 1}')
