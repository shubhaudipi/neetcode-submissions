class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):  
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif sum < target: 
                    l += 1
                else:
                    r -= 1
               
            
        return res



