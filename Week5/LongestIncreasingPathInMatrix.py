class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.memo = {}
        maxresult = 0
        if matrix == []:
            return maxresult
        lx = len(matrix)
        ly = len(matrix[0])
        def _lIP(x,y, length):
            if self.memo.get((x,y)):
                return self.memo[(x,y)]
            
            mlen = length
            if x-1 >= 0 and matrix[x-1][y]> matrix[x][y]:
                mlen = max(mlen, _lIP(x-1,y,length)+1)
            if y-1 >= 0 and matrix[x][y-1]> matrix[x][y]:
                mlen = max(mlen, _lIP(x,y-1,length)+1)
            if x+1 < lx and matrix[x+1][y]> matrix[x][y]:
                mlen = max(mlen, _lIP(x+1,y,length)+1)
            if y+1 < ly and matrix[x][y+1]> matrix[x][y]:
                mlen = max(mlen, _lIP(x,y+1,length)+1)
            
            self.memo[(x,y)] = mlen
            return mlen
            
            
        
        for x in range(lx):
            for y in range(ly):
                maxresult = max(maxresult ,_lIP(x,y,1))
        
        return maxresult
