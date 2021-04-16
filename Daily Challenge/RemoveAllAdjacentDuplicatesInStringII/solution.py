class Solution:
    def k_adjacent(self, s,k):
        count = 0
        previous = ""
        i_prev = None
        n = len(s)
        if(n<k): 
            return False, 0
        
        for i in range(n):
            if(count == k):
                return True, i_prev
            if(s[i] == previous):
                count+=1
            else:
                previous = s[i]
                count = 1
                i_prev = i
        return (count == k), i_prev
    
    def removeDuplicates(self, s: str, k: int) -> str:
        
        is_k, i_val = self.k_adjacent(s,k)
        
        while(is_k):
            s = s[:i_val]+s[i_val+k:]
            is_k, i_val = self.k_adjacent(s,k)
        return s
