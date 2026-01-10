class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        maxAr = 0
        # start at opposite ends to maximize width
        while l < r:
            currArea = abs(r-l) * min(height[r], height[l])
            maxAr = currArea if currArea >= maxAr else maxAr
            # move pointer for lower line since height must be min. between them b/c
            # area can't be slanted
            if height[r] < height[l]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return maxAr



