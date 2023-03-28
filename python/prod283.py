from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_available_pos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pass
            else:
                nums[next_available_pos], nums[i] = nums[i], nums[next_available_pos]
                next_available_pos += 1
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
    print(s.moveZeroes([0]))
