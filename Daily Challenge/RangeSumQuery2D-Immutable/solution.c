typedef struct {
    int** M;    
} NumMatrix;


NumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {
    
    NumMatrix* mat = malloc(sizeof(NumMatrix));
    int **myMatrix = (int **)malloc(matrixSize * sizeof(int*));

    for(int i = 0; i < matrixSize; i++)
        myMatrix[i] = (int *)malloc(matrixColSize[i] * sizeof(int));
    
    mat->M = myMatrix;
    
    for(int i = 0; i < matrixSize; i++)
       for(int j = 0; j < matrixColSize[0]; j++)
           mat->M[i][j] = matrix[i][j] + (i>0?mat->M[i-1][j]:0);

        
    for(int i = 0; i < matrixSize; i++)
        for(int j = 1; j < matrixColSize[0]; j++)
           mat->M[i][j] += mat->M[i][j-1]; 

        
    return mat;
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    return obj->M[row2][col2] - (col1>0?obj->M[row2][col1-1]:0) - (row1>0?obj->M[row1-1][col2]:0) + ((row1>0)&&(col1>0)?obj->M[row1-1][col1-1]:0);
}

void numMatrixFree(NumMatrix* obj) {
    free(obj->M);
    free(obj);
}

/**
 * Your NumMatrix struct will be instantiated and called as such:
 * NumMatrix* obj = numMatrixCreate(matrix, matrixSize, matrixColSize);
 * int param_1 = numMatrixSumRegion(obj, row1, col1, row2, col2);
 
 * numMatrixFree(obj);
*/
