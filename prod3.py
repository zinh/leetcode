class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = longest = 1
        l = len(s)
        pointer = 1
        h = { s[0] }
        while pointer < l:
            c = s[pointer]
            print(h, c, result)
            if c in h:
                result -= 1
            else:
                h.add(c)
                result += 1
                if longest < result:
                    longest = result
            pointer += 1
        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcd'))
