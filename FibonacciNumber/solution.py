class Solution:
    def fib(self, n: int) -> int:
        if n==0 : return 0
        
        L = [0]*(n+1)
        L[1]=1
        
        for i in range(2,n+1):
            L[i]=L[i-1]+L[i-2]
            
        return L[n]
