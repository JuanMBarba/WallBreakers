class UnionFind:
    
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        
        if x_root == y_root:
            return
            
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] = self.rank[y_root] + 1
    
    
    
    

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        
        lengthX = len(board)
        lengthY = len(board[0])
        
        UFBoard = UnionFind(lengthX*lengthY)
        
        notFlipped = set()
        
        for x in range(lengthX):
            for y in range(lengthY):

                if board[x][y]=="O":
                    try:  
                        if board[x][y+1] == "O":
                            UFBoard.union(x*lengthY+y,x*lengthY+y+1) 
                    except:
                        pass
                    
                    try:
                        if board[x+1][y] == "O":
                            UFBoard.union(x*lengthY+y,(x+1)*lengthY+y)
                    except:
                        pass
                    
                    if x == 0 or y == 0 or x == lengthX-1 or y == lengthY-1:
                        notFlipped.add(UFBoard.find(x*lengthY+y))
                else:
                    UFBoard.parent[x*lengthY+y] = -1

        notFlipped = set([UFBoard.find(x) for x in notFlipped])
        
        for x in range(lengthX):
            for y in range(lengthY):
                if board[x][y]=="O":
                    if UFBoard.find(x*lengthY+y) not in notFlipped:
                        board[x][y]="X"
