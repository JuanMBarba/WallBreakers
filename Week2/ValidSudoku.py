class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        
        def validSegment(segment: List[str]) -> bool:
            dd = defaultdict(int)
            
            for item in segment:
                dd[item]+=1
                if item != "." and dd[item] > 1:
                    return False
            
            return True
        
        for index in range(9):
            'Row'
            
            if not validSegment(board[index]):
                return False
            'Column'            
            if not validSegment([x[index] for x in board]):
                return False
            'Sub-Box'
            subbox = []
            for x in board[(index%3*3):(index%3*3+3)]:
                subbox = subbox+x[index//3*3:index//3*3+3]
            
            if not validSegment(subbox):
                return False
            
        return True
