class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        i = n-2
        while(i >= 0):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
            i-=1
        return triangle[0][0]
