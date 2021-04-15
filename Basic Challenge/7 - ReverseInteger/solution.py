class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        
        s = str(x)
        sign = 1
        if(s[0]=="-"):
            sign = -1
            s = s[1:]
        s = s[::-1]
        while(s[0]=="0"):
            s = s[1:]
            
        numb = int(s)
        if(numb<-2**31 or numb>2**31-1):
            return 0
        return sign * numb
