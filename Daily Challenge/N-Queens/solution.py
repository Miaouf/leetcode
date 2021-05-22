class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
        
        def translate_solve(ans):
            final_ans = []
            for L in ans:
                if(L == []):
                    continue
                else:
                    c_ans = []
                    for i in range(n):
                        temp = ""
                        for j in range(n):
                            temp+= "Q" if L[i][j]==2 else "."
                        c_ans.append(temp)
                    final_ans.append(c_ans)
            if(final_ans == []):
                return []
            else :
                return final_ans
        
        return translate_solve(rec_solve(board,n,0,[]))
