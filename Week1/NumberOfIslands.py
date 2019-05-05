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
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid == []:
            return 0
        
        lengthX = len(grid)
        lengthY = len(grid[0])
        
        UFGrid = UnionFind(lengthX*lengthY)
        
        
        for x in range(lengthX):
            for y in range(lengthY):
                if grid[x][y]=="1":
                    try:  
                        if grid[x][y+1] == "1":
                            UFGrid.union(x*lengthY+y,x*lengthY+y+1) 
                    except:
                        pass
                    try:
                        if grid[x+1][y] == "1":
                            UFGrid.union(x*lengthY+y,(x+1)*lengthY+y)
                    except:
                        pass
                else:
                    UFGrid.parent[x*lengthY+y] = -1
        
        return len(set([UFGrid.find(x) for x in range(lengthX*lengthY)])-{-1})
