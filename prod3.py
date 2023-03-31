class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = len(s)
        if L == 0:
            return 0
        start = 0
        pointer = start + 1
        h = { s[0] }
        m = 1
        while pointer < L:
            c = s[pointer]
            if c in h:
                h.discard(s[start])
                start += 1
            else:
                h.add(c)
                pointer += 1
                if m < (pointer - start):
                    m = (pointer - start)
        return m

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('pwwkew'))
