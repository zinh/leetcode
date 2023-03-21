from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        # print(start, end)
        if (end - start) <= 1:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1
        middle = (start + end) >> 1
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self.binary_search(nums, target, start, middle)
        else:
            return self.binary_search(nums, target, middle, end)

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 2))
