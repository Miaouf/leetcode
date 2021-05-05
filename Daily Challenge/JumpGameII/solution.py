class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def rec(nums,ans):
            n = len(nums)
            if(nums[0] == 0 or n == 1):
                return 0
            
            if(nums[0] >= n-1):
                return ans+1
            else:
                next = []
                for i in range(1,nums[0]+1):
                    next.append(i+nums[i])
                return rec(nums[next.index(max(next))+1:],ans+1)

        return rec(nums,0)
