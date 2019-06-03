class Solution:
    def isValidSudoku(self,i,row,column, board: List[List[str]]) -> bool:
        if i in board[row]:
            return False
        
        if i in [x[column] for x in board]:
            return False
        
        r_ = (row // 3) * 3
        c_ = (column // 3) * 3
        b_ = [board[x][c_:c_ + 3] for x in range(r_, r_ + 3)]
        for b_row in b_:
            if i in b_row:
                return False
        return True
        
    
    def fullBoard(self, board:List[List[str]])->bool:
        for x in board:
            for y in x:
                if y == ".":
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #if self.fullBoard(board):
        #return
        stop = True
        
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    stop = False
                    break
            if board[x][y] == ".":
                break
        
        if stop:
            return
        
        for i in range(1,10):
            if self.isValidSudoku(str(i),x,y,board):
                board[x][y]= str(i)
                self.solveSudoku(board)
                if self.fullBoard(board):
                    return
                
            board[x][y] = "."
