class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lx = len(board)
        ly = len(board[0])
        
        def _wordsearch(index,x,y):
            if word[index:] == "":
                return True
            if x-1 >= 0 and board[x-1][y] == word[index]:
                temp = board[x-1][y]
                board[x-1][y] = "!"
                if _wordsearch(index+1, x-1, y):
                    return True
                board[x-1][y] = temp
            if x+1 < lx and board[x+1][y] == word[index]:
                temp = board[x+1][y]
                board[x+1][y] = "!"
                if _wordsearch(index+1, x+1, y):
                    return True
                board[x+1][y] = temp

            if y-1 >= 0 and board[x][y-1] == word[index]:

                temp = board[x][y-1]
                board[x][y-1] = "!"
                if _wordsearch(index+1, x, y-1):
                    return True
                board[x][y-1] = temp
            if y+1 < ly and board[x][y+1] == word[index]:
                temp = board[x][y+1]
                board[x][y+1] = "!"
                if _wordsearch(index+1, x, y+1):
                    return True
                board[x][y+1] = temp
            
            return False
        
        for x in range(lx):
            for y in range(ly):
                if board[x][y] == word[0]:
                    temp = board[x][y]
                    board[x][y] = "!"
                    if _wordsearch(1,x,y):
                       return True
                    board[x][y] = temp
        
        return False
