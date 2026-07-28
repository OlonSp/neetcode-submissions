class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab = dict()
        for i in range(len(nums)):
            for k in tab.keys():
                if tab[k] == nums[i]:
                    return [k, i]
            
            diff = target - nums[i]
            tab[i] = diff
