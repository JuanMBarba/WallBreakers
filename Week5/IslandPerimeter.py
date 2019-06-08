class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def checkAround(grid, x,y, mx,my):
            result = 0
            if x-1 < 0 or grid[x-1][y] == 0:
                result+=1
            if x+1 == mx or grid[x+1][y] == 0:
                result+=1
            if y-1 < 0 or grid[x][y-1] == 0:
                result+=1
            if y+1 == my or grid[x][y+1] == 0:
                result+=1
            return result
        
        mx = len(grid)
        my = len(grid[0])
        result = 0
        for x in range(mx):
            for y in range(my):
                if grid[x][y]==1:
                    result+= checkAround(grid,x,y,mx,my)
        return result
