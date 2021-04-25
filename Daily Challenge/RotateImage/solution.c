void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int buffer;
    //Transpose
    for(int i = 0; i < matrixSize-1; i++){
        for(int j = i+1; j < matrixSize; j++){
            buffer = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = buffer;
        }
    }
    
    //Swap col
    for(int j = 0; j < matrixSize/2; j++){
        for(int i = 0; i < matrixSize; i++){
            buffer = matrix[i][j];
            matrix[i][j] = matrix[i][matrixSize-1-j];
            matrix[i][matrixSize-1-j] = buffer;
        }
    }    
}
