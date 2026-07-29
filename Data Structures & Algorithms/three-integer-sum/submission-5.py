class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        sort_nums = sorted(nums)
        if sort_nums[0] > 0 or sort_nums[-1] < 0:
            return []
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                var = sort_nums[i] + sort_nums[l] + sort_nums[r]
                if var > 0:
                    r -= 1
                elif var < 0:
                    l += 1
                else:
                    if [sort_nums[i], sort_nums[l], sort_nums[r]] not in ans:
                        ans.append([sort_nums[i], sort_nums[l], sort_nums[r]])
                    r -= 1
        
        return ans