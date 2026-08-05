import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        freqs = {}
        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        
        for num in freqs.keys():
            heapq.heappush(minheap, (freqs[num], num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])

        return res
        