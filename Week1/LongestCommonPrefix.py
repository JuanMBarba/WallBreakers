class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ''
        
        tupleSize = len(strs)
        
        if tupleSize == 1:
            return strs[0]
        
        
        for x in zip(*strs):
            if tupleSize != len(x):
                break
                
            for y in range(tupleSize-1):
                if x[y] != x[y+1]:
                    return prefix
                elif y == tupleSize-2:
                    prefix+=x[y]
            
        
        return prefix
            
        
        
        '''
        if tupleSize == 0:
            return prefix
        
        minLength = min(len(x) for x in strs)
        
        position = 0    
            
        for x in range(minLength):
            
            for y in range(tupleSize-1):
                if strs[y][x] != strs[y+1][x]:
                    return prefix
                elif y == tupleSize-2:
                    prefix+=strs[y][x]
        
        return prefix
        ''' 
