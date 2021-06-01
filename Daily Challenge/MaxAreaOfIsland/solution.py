class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        def island_area(i,j):
            if(i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0):
                return 0
            else:
                grid[i][j] = 0
                return 1 + island_area(i-1,j) + island_area(i+1,j) + island_area(i,j-1) + island_area(i,j+1)
              
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    ans = max(ans, island_area(i,j))
        
        return ans
