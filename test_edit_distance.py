import unittest
from edit_distance import distance

class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        testcases = [
                {'input': ['aa', 'aa'], 'expected': 0},
                {'input': ['aa', 'bb'], 'expected': 4},
                ]
        for testcase in testcases:
            inp = testcase['input']
            expected = testcase['expected']
            output = distance(inp[0], inp[1])
            self.assertEqual(expected, output)
