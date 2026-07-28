class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for elem in nums:
            if elem not in res.keys():
                res[elem] = 1
            else:
                res[elem] += 1
        freq = [[] for i in range(len(nums)+1)]
        for key in res.keys():
            freq[res[key]].append(key)
        ans = []
        for elems in freq[::-1]:
                for elem in elems:
                    ans.append(elem)
                    if len(ans) == k:
                        return ans


