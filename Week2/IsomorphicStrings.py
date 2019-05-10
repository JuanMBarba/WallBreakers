class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        ddS = defaultdict(int)
        ddT = defaultdict(int)
        
        for i, (x,y) in enumerate(zip(s, t)):
            if ddS[x] == 0:
                ddS[x]=i+1
            if ddT[y] == 0:
                ddT[y]=i+1         
            if ddS[x] != ddT[y]:
                return False
        
        return True
