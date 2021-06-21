class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if(i == 0):
                ans.append([1])
            elif(i == 1):
                ans.append([1,1])
            else:
                L = [1]
                for j in range(i-1):
                    L.append(ans[-1][j]+ans[-1][j+1])
                L.append(1)
                ans.append(L)
        return ans
        
