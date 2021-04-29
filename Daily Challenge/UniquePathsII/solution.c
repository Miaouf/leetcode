int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    if(obstacleGrid[0][0] == 1){
        return 0;
    }else{
        obstacleGrid[0][0] = 1;
    }

    for(int i = 0; i < obstacleGridSize; i++){
        for(int j = 0; j < obstacleGridColSize[i]; j++){
            if(i == 0 && j == 0){
                ;
            }else{
                if(obstacleGrid[i][j] == 1){
                    obstacleGrid[i][j] = 0;
                }else{
                    obstacleGrid[i][j] = (i>0?obstacleGrid[i-1][j]:0) + (j>0?obstacleGrid[i][j-1]:0);
                }
            }
        }
    }
    
    return obstacleGrid[obstacleGridSize-1][obstacleGridColSize[0]-1];
}
