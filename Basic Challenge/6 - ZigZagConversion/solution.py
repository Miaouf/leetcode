class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        new_s = ""
        k=0
        n = len(s)
        while(k<numRows-1):
            i = k
            cpt = 0
            while(i < n):
                new_s += s[i]
                i += 2*(numRows-1-k)
                if(i < n and k!=0):
                    new_s += s[i]
                    i += 2*k         
            k+=1
        i = numRows-1
        while(i < n):
            new_s += s[i]
            i += 2*(numRows-1)  
        return new_s
