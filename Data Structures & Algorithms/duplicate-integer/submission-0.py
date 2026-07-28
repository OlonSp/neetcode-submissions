class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni = set()
        flag = False
        for num in nums:
            if num in uni:
                return True
            uni.add(num)
        return False
                

        