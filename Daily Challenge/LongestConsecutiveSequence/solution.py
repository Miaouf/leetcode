class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        nums = set(nums)
        heap = []
        heapify(heap)
        for num in nums :
            heappush(heap,num)
        
        ans = 0
        cpt = 1
        prev = heappop(heap)
        while(heap != []):
            temp = heappop(heap)
            if(prev+1 == temp):
                cpt += 1
                prev += 1
            else:
                ans = max(ans,cpt)
                cpt = 1
                prev = temp
        
        return max(ans,cpt)
