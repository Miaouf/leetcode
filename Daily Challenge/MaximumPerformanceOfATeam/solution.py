class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(efficiency,speed)
        engineers = sorted(engineers, key = lambda x : x[0], reverse = True)

        heap = []
        heapify(heap)
        
        ans = 0
        max_speed = 0
        
        for eff, spd in engineers:
            heappush(heap,spd)
            max_speed += spd
            
            if(len(heap) > k):
                max_speed -= heappop(heap)
                
            ans = max(ans, max_speed*eff)
            

        return ans%(10**9 + 7)
