#define min(x,y) (x < y ? x : y)

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
        for(int i = triangleSize-2; i>=0; i--){
           for(int j = 0; j<i+1; j++){
               triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]);
            }  
        }
        return triangle[0][0];
}
