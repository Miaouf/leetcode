class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        
        ans = 0
        prev = 0
        ind = 1
        
        for i in range(1,n):
            if(s[i]==s[i-1]):
                ind+=1
            else:
                ans += min(prev,ind)
                prev = ind
                ind = 1

        return ans + min(prev,ind)
