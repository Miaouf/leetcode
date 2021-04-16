class Solution:
    def k_adjacent(self, s,k):
        count = 1
        i_prev = 0
        n = len(s)
        
        if(n<k): return False, 0
        
        for i in range(1,n):
            if(count == k):
                return True, i_prev
            if(s[i] == s[i_prev]):
                count+=1
            else:
                count = 1
                i_prev = i
                
        return (count == k), i_prev
    
    def removeDuplicates(self, s: str, k: int) -> str:
        
        is_k, i_val = self.k_adjacent(s,k)
        
        while(is_k):
            s = s[:i_val]+s[i_val+k:]
            is_k, i_val = self.k_adjacent(s,k)
        return s
