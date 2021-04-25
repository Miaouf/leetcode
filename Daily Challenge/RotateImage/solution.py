class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n//2):
            for j in range(i,n-1-i):
                ind_i, ind_j = i, j
                buffer = matrix[i][j]
                for _ in range(4):
                    buffer, matrix[ind_j][n-1-ind_i] = matrix[ind_j][n-1-ind_i], buffer
                    ind_i, ind_j = ind_j, n-1-ind_i
