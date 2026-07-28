class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alp = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            alp[ord(s[i]) - ord('a')] += 1
            alp[ord(t[i]) - ord('a')] -= 1
        for elem in alp:
            if elem != 0:
                return False
        
        return True