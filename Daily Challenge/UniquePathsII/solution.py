class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
       
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if(i==0 and j ==0):
                    obstacleGrid[i][j] = (obstacleGrid[i][j]+1)%2
                    
                elif obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] if i != 0 else 0)\
                                        +(obstacleGrid[i][j-1] if j != 0 else 0)
                else : 
                    obstacleGrid[i][j] = 0

        return obstacleGrid[-1][-1]
