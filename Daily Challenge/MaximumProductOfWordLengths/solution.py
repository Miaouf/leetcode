class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                share = False
                for c in words[i]:
                    if(c in words[j]):
                        share = True
                        break
                if(share == False):
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
