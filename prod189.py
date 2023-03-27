from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        return [nums[((l - k) + i) % l] for i in range(0, l)]

class Solution2:
    def find_next_pos(self, pos: int, k: int, l: int) -> int:
        '''
        return the position that pos needed to switch with
        '''
        # middle will switch with 0
        # item before middle will switch with item + k
        # item after middle with switch with ?
        middle = l - k
        if pos < middle:
            return pos + k
        else:
            return pos - middle

    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        tmp = nums[0]
        next_pos = 0
        for _ in range(l):
            print(next_pos)
            next_pos = self.find_next_pos(next_pos, k, l)
            nums[next_pos], tmp = tmp, nums[next_pos]
        return nums


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[::] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums

if __name__ == "__main__":
    s = Solution2()
    results = s.rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(results)
