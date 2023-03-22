from typing import List
from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0] ** 2]
        results = deque()

        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            direction = -1
            pos, op_pos = len(nums) - 1, 0
        else:
            direction = 1
            pos, op_pos = 0, len(nums) - 1
        while True:
            # print(pos, op_pos)
            if abs(nums[pos]) >= abs(nums[op_pos]):
                results.appendleft(nums[pos] ** 2)
                pos += direction
            else:
                direction = -direction
                pos, op_pos = op_pos, pos
            if pos == op_pos:
                results.appendleft(nums[pos] ** 2)
                break
        return list(results)

if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedSquares([-7,-3,2,3,11]))
