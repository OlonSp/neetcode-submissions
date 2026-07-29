class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                var = nums[i] + nums[l] + nums[r]
                if var > 0:
                    r -= 1
                elif var < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
        
        return ans