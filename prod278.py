# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    if version == 4:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.first_bad_version(1, n)

    def first_bad_version(self, start: int, end: int) -> int:
        print(start, end)
        if (end - start) <= 1:
            if isBadVersion(start):
                return start
            return end
        middle = (end + start) >> 1
        if isBadVersion(middle):
            return self.first_bad_version(start, middle)
        else:
            return self.first_bad_version(middle, end)

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstBadVersion(5))
