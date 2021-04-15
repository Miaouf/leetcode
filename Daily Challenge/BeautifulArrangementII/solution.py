class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        L = list(range(1,n+1))
        i = 1
        while(k>2):
            L = L[:i]+[L[-1]]+L[i:-1]
            i += 2
            k -= 2
        if(k==2):
            L[-1],L[-2] = L[-2],L[-1]
        return L
