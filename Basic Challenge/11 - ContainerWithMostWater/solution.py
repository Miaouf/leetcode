class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        i = 0
        j = len(height)-1
        h_max = max(height)
        while(j > i):
            if(h_max*(j-i) <= water):
                return water
            if(height[i] <= height[j]):
                water = max(water, (j-i)*height[i])
                i+=1
            else:
                water = max(water, (j-i)*height[j])
                j-=1
        return water
