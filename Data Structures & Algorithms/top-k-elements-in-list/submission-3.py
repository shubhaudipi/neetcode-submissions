class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        map = [[] for i in range(len(nums) + 1)]

        for num in freqs:
            map[freqs[num]].append(num)

        res = []

        for i in range(len(map)-1, 0, -1): 
            res.extend(map[i])
            if len(res) == k: 
                return res






        