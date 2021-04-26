# Pure python solution without any library
# Can be optimize using heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)-1
        max_jumps = [0]*ladders
        min_max_jumps = 0
        summ = 0
        L = []
        ans = 0
        for i in range(n):
            if(ladders >= n-i):
                return n
            
            diff = heights[i+1]-heights[i]
            
            if(diff > 0):
                L.append(diff)
                summ += diff
                
                if(summ > bricks):
                    ladders -= 1
                    summ -= L.pop(L.index(max(L))) 
                    
                if(summ > bricks or ladders < 0):
                    return i
            
        return n
