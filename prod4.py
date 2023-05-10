from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        p1 = p2 = 0
        result = []
        while True:
            if p1 >= n1 or p2 >= n2:
                break
            if nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
        if p1 >= n1:
            a = nums2
            pointer = p2
        if p2 >= n2:
            a = nums1
            pointer = p1
        # print(result,a,pointer)
        def get_val(idx):
            if idx < (p1 + p2):
                return result[idx]
            else:
                delta = idx - p1 - p2
                return a[pointer + delta]
        if (n1 + n2) % 2 == 0:
            right = (n1 + n2) // 2
            left = right - 1
            # print(left,right, get_val(left),get_val(right))
            return (get_val(left) + get_val(right)) / 2
        else:
            m = (n1 + n2) // 2
            return float(get_val(m))

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([],[1]))
