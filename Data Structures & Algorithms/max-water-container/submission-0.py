class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j= 0, len(heights)-1
        max_water = 0
        while i<j:
            h = min(heights[i], heights[j])
            w = j-i
            max_water = max(max_water, h*w)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water
        