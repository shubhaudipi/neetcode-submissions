class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)

        prodp = 1
        for i in range(len(nums)): 
            prefix[i] = prodp
            prodp *= nums[i]

        prods = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = prods
            prods *= nums[i]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res


        

        