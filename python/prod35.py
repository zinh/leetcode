from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search_insert_binary(nums, target, 0, len(nums) - 1)

    def search_insert_binary(self, nums: List[int], target: int, start: int, end: int):
        if (end - start) <= 1:
            if nums[start] >= target:
                return start
            if nums[end] >= target:
                return end
            else:
                return end + 1
        middle = (end + start) >> 1
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            return self.search_insert_binary(nums, target, start, middle)
        if nums[middle] < target:
            return self.search_insert_binary(nums, target, middle, end)

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 7))
