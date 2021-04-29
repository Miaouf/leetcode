#Compact 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target not in nums):
            return [-1, -1]
        else:
            return [nums.index(target), len(nums)-1-nums[::-1].index(target)]

'''
#Recursive 
def rec(nums, i, j, target):
    mid = (i+j)//2
    
    if(nums[mid] == target):
        s_ind = mid
        e_ind = mid
        while(s_ind-1 >= i and nums[s_ind-1] == target):
            s_ind -= 1
        while(e_ind+1 <= j and nums[e_ind+1] == target):
            e_ind += 1
        return [s_ind,e_ind]
    
    if(mid == i == j):
        return [-1, -1]
    
    elif(nums[mid] > target):
        return rec(nums, i, mid-1, target)
    
    else:
        return rec(nums, mid+1, j, target)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target not in nums):
            return [-1, -1]
        else:
            return rec(nums, 0, len(nums)-1, target)
'''

'''
#Iterative
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target not in nums):
            return [-1, -1]
        
        i = 0
        j = len(nums)-1
        
        while(i != j):
            mid = (i+j)//2

            if(nums[mid] == target):
                s_ind = mid
                e_ind = mid
                
                while(s_ind-1 >= i and nums[s_ind-1] == target):
                    s_ind -= 1
                    
                while(e_ind+1 <= j and nums[e_ind+1] == target):
                    e_ind += 1
                    
                return [s_ind,e_ind]

            elif(nums[mid] > target):
                j = mid - 1

            else:
                i = mid + 1

        if(nums[i] == target):
            return [i,j]
        else:
            return [-1,-1]
'''
