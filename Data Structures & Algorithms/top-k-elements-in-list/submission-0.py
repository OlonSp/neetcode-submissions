class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for elem in nums:
            if elem not in res.keys():
                res[elem] = 1
            else:
                res[elem] += 1
        sorted_dict = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        return [list(sorted_dict.keys())[i] for i in range(k)]