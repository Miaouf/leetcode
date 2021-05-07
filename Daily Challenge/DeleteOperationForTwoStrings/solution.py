class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        
        #Longuest Common Subsequence (LCS)
        M = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(word1[i-1] == word2[j-1]):
                    M[i][j] = 1 + M[i-1][j-1]
                else:
                    M[i][j] = max(M[i-1][j], M[i][j-1])
                    
        return n1+n2-2*M[n1][n2]
        
