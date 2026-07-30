class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxLen = 0
        while r < len(s):
            print(l, r)
            if s[r] not in s[l:r]:
              r += 1
            else:
              maxLen = max(maxLen, r-l)
              while s[r] in s[l:r]:
                l += 1
        maxLen = max(maxLen, r-l)
        return maxLen