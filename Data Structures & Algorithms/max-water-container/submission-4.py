class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVol = 0
        
        while l < r:
            # 1. Calculate the current area once
            currentVol = (r - l) * min(heights[l], heights[r])
            
            # 2. Update maxVol using the built-in max function
            maxVol = max(maxVol, currentVol)
            
            # 3. Move the pointers (with 'else' handling the equal case)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return maxVol