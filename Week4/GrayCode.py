class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        gc = self.grayCode(n-1)
        result = []
        for x in gc[::-1]:
            result.append(x + (2**(n-1))
            
        return gc+result
