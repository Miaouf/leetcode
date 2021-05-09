"""
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        while(target != [1]*len(target)):            
            max_v = max(target)
            ind = target.index(max_v)
            summ = sum(target)-max_v

            if(summ == 1):
                return True
            
            elif(summ >= target[ind] or summ == 0):
                return False
            
            else:
                target[ind] = target[ind]%summ
            
        
        return True
"""

class Solution:
    def isPossible(self, target: List[int]) -> bool:       
        heap = []
        
        for t in target:
            heapq.heappush(heap, -t)
            
        summ = -sum(heap) + heap[0]
        
        while(heap[0] != -1):   
            max_v = -heapq.heappop(heap)
            
            if(summ == 1):
                return True
            
            elif(summ >= max_v or summ == 0):
                return False
            
            else:
                heapq.heappush(heap, -(max_v%summ))
                summ += (heap[0]+(max_v%summ))
        
        return True
