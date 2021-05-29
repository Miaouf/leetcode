class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [[1]*n for _ in range(n)]
        def update(board,i,j):
            for k in range(n):
                board[i][k] = 0 #Row
                board[k][j] = 0 #Col
                
                if(i-k >= 0 and j-k >= 0):
                    board[i-k][j-k] = 0 #Diag1
                elif(i+(k-min(i,j)) < n and j+(k-min(i,j)) < n):
                     board[i+(k-min(i,j))][j+(k-min(i,j))] = 0 #Diag1
                else:
                    pass
                    
                if(i-k >= 0 and j+k < n):
                    board[i-k][j+k] = 0 #Diag1
                elif(i+(k-min(i,n-(j+1))) < n and j-(k-min(i,n-(j+1))) >= 0):
                     board[i+(k-min(i,n-(j+1)))][j-(k-min(i,n-(j+1)))] = 0 #Diag1
                else:
                    pass
                
            board[i][j] = 2
            return board
        
        def rec_solve(board, n, queen, ans):
            if(n == queen):
                return ans+[board]
            
            for j in range(n):
                if(board[queen][j] == 1):
                    ans = rec_solve(update([row[:] for row in board],queen,j),n,queen+1,ans)
            return ans  
     
        return len(rec_solve(board,n,0,[]))
