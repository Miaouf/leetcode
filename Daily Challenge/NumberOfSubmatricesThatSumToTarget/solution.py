class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])
        
        #Prefix matrix by row
        for i in range(1,n_row):
            for j in range(n_col): 
                matrix[i][j] += matrix[i-1][j]
                
        
        numb = 0
        
        for i_s in range(n_row):
            for i_e in range(i_s,n_row):
                dico = {}
                dico[0] = 1
                summ = 0

                for j in range(n_col):
                    
                    summ += matrix[i_e][j] - (matrix[i_s-1][j] if i_s!=0 else 0)
                    
                    if (summ-target) in dico:
                        numb += dico[summ-target]
                        
                    if(summ in dico):
                        dico[summ]+=1
                        
                    else:
                        dico[summ] = 1
                
        return numb
