import unittest
from prod3 import Solution

class TestProd19(unittest.TestCase):
    def test_prod_19(self):
        testcases = [
                {'input': ["abcabcbb"], 'expected': 3},
                {'input': ["bbbbb"], 'expected': 1},
                {'input': ["pwwkew"], 'expected': 3},
                ]
        for idx, testcase in enumerate(testcases):
            solution = Solution()
            actual = solution.lengthOfLongestSubstring(testcase['input'][0])
            self.assertEqual(testcase['expected'], actual, f'testcase {idx}')
