def isPalindrome(s, i, j):
    while(i < j):
        if(s[i] != s[j]):
            return False
        i+=1
        j-=1
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        pal = s[0]
        cur_n = 1
        pal_n = 1
        while(cur_n < n):
            idx = 0
            while((idx + cur_n) < n):
                if(cur_n > pal_n + 2):
                    return pal

                elif(isPalindrome(s,idx,idx+cur_n)):
                    pal = s[idx:idx+cur_n+1]
                    pal_n = cur_n
                    break
                else:
                    idx+=1
            cur_n+=1
        return pal
                  
