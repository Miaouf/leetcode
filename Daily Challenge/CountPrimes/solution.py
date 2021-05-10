class Solution:
    def countPrimes(self, n: int) -> int:        
        if(n <= 2):
            return 0
                
        isPrime = [True]*n
        isPrime[0], isPrime[1] = False, False
        
        ans = 0
        
        for i in range(2,n):
            if isPrime[i] == False:
                pass
    
            else:
                ans+=1
                for k in range(i,n,i):
                    isPrime[k] = False                
        return ans
        
