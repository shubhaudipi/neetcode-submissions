class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max = 0 
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            cur = width * height
            if cur > max:
                max = cur
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max


        