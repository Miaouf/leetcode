def sol(nums,target,L):
    if(target == 0):
        return 1
    elif(L[target] != -1): #Not seen before
        return L[target]
    else:
        L[target] = 0
        for i in nums :
            if i<=target:
                L[target] += sol(nums,target-i,L)
    return L[target]

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        L = [-1]*(target+1)
        return sol(nums,target,L)
