class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = {}
        for i, n in enumerate(nums): 
            ndict[n] = i; 

        for i in range(len(nums)): 
            if (target - nums[i] in ndict) and (ndict.get(target - nums[i]) > i):
                return [i, ndict.get(target - nums[i])]



        