class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        high = 0
        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                count = 0
                curr = nums[i]
                while curr in numset:
                    count += 1
                    curr += 1
                if count > high:
                    high = count
        
        return high
        