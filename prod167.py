from typing import List
'''
Memory constrain: O(1)
numbers: non-decreasing order
'''
class Solution:
    def binary_search(self, numbers, start, end, n):
        while True:
            if start >= end:
                if numbers[start] == n:
                    return start
                else:
                    return None
            middle = (start + end) // 2
            if numbers[middle] == n:
                return middle
            elif numbers[middle] > n:
                end = middle - 1
            else:
                start = middle + 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            j = self.binary_search(numbers, i + 1, len(numbers) - 1, target - numbers[i])
            if j is not None:
                return [i + 1, j + 1]
        return None

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left +1, right + 1]
            if s > target:
                right -= 1
            else:
                left += 1

if __name__ == '__main__':
    s = Solution2()
    print(s.twoSum([-1, -1, -1, -1, 1, 1], 2))
