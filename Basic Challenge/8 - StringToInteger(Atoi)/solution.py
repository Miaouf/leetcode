class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = ""
        while(i<n and s[i]==" "):
            i+=1
        
        if(i==n):
            return 0
        
        if(s[i]=="-"):
            sign = -1
            i+=1
        elif(s[i]=="+"):
            i+=1 
        
        while(i<n and s[i].isdigit()):
            num += s[i]
            i += 1
            
        if(num == ""):
            return 0
        
        num = int(num)*sign
        if(num < -2**31):
            num = -2**31
        elif(num > 2**31 -1):
            num = 2**31-1
            
        return num
