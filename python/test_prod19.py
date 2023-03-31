import unittest
from prod19 import Solution
from python.prod876 import ListNode 

class TestProd19(unittest.TestCase):
    def test_prod_19(self):
        testcases = [
                {'input': [[1,2,3,4,5], 2], 'expected': [1,2,3,5]},
                # {'input': [[1], 1], 'expected': []},
                {'input': [[1,2], 1], 'expected': [1]},
                {'input': [[1,2], 2], 'expected': [2]},
                ]
        for idx, testcase in enumerate(testcases):
            solution = Solution()
            actual = solution.removeNthFromEnd(ListNode.from_list(testcase['input'][0]), testcase['input'][1])
            self.assertEqual(testcase['expected'], list(actual), f'testcase {idx}')
