class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        
        ans = 0
        
        for i in range(100000): # left,right <= 10^18  -> sqrt <= 10^9 -> s1 < 10^5
            s1 = str(i)
            s2 = s1[::-1]
            num = int(s1+s2)**2
            
            if(num < left):
                pass
            elif(num > right):
                break
            else:
                if(str(num) == str(num)[::-1]):
                    ans+=1
        
        for i in range(100000):
            s1 = str(i)
            s2 = s1[-2::-1]
            num = int(s1+s2)**2
            
            if(num < left):
                pass
            elif(num > right):
                break
            else:
                if(str(num) == str(num)[::-1]):
                    ans+=1
                    
        return ans
