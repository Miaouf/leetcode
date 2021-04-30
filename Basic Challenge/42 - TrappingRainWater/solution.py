class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        S = []
        E = []
        n = len(height)
        
        if(n==0):
            return 0
        
        max_v = height[0] #Height max from the left 
        for i in range(1,n-1):
            max_v = max(max_v,height[i])
            S.append(max_v)
            
        max_v = height[-1] #Height max from the right
        for i in range(n-2,0,-1):
            max_v = max(max_v,height[i])
            E.append(max_v)
        
        full = [min(S[i],E[n-3-i]) for i in range(0,n-2)]

        return sum([full[i-1]-height[i] for i in range(1,n-1)])
