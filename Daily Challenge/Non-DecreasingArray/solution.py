class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        first = True
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                if(first == True):
                    first = False
                else:
                    return False
                    
                if(i == 0 or nums[i-1]<=nums[i+1]):
                    pass
                else:
                    nums[i+1] = nums[i]
        return True
