class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        most = defaultdict(list)
        for i in nums: 
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        for num in counts:
            most[counts[num]].append(num)

        finalkeys = sorted(most.keys(), reverse=True)
        final = []
        for key in finalkeys:
            if (len(final) < k):
                final.extend(most[key])

        return final
        

            

        