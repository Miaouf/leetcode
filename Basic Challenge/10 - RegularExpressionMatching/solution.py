def my_sol(s,p,prev):
    len_s = len(s)
    len_p = len(p)
    i = 0
    j = 0
    while(i<len_s and j<len_p):
        if(p[j] == "." or p[j]==s[i]):
            sol = my_sol(s[i+1:],p[j+1:],p[j])
            if(sol == True):
                return sol
            if(j+1 < len_p and p[j+1]=="*"):
                return my_sol(s[i:],p[j+2:],p[j+1])
            return False
        elif(p[j]=="*"):
            sol = my_sol(s[i:],prev+p[j:],prev)
            if(sol == True):
                return sol
            return my_sol(s[i:],p[j+1:],p[j])
        elif((j+1 < len_p) and p[j+1]=="*"):
            return my_sol(s[i:],p[j+2:],p[j+1])
            
        else:
            return False
    
    if(j < len_p and p[j]=="*"):
        j+=1
    while((j+1 < len_p) and p[j+1]=="*"):
        j+=2  
    return i==len_s and j==len_p
    

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        for k in range(len(p)):
            if((p[k]!="*" and p[k]!=".") and p[k] not in s and not ((k+1 < len(p)) and p[k+1]=="*")):
                return False
        return my_sol(s,p,"")
