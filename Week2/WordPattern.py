class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        
        ddP = defaultdict(int)
        ddS = defaultdict(int)
        
        sList = s.split()
        
        if len(sList) != len(pattern):
            return False
        
        for i, (x,y) in enumerate(zip(pattern, sList)):
            if ddP[x] == 0:
                ddP[x]=i+1
            if ddS[y] == 0:
                ddS[y]=i+1
            if ddP[x] != ddS[y]:
                return False
        
        return True
