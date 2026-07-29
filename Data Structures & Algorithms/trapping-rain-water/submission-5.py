class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix = []
        suffix = []
        maxi = 0
        for i in range(len(height)):
            maxi = max(maxi, height[i])
            prefix.append(maxi)
        maxi = 0
        for i in range(len(height)-1, -1, -1):
            maxi = max(maxi, height[i])
            suffix.append(maxi)
        suffix.reverse()
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i]
        return res