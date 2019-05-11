class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        counterS=Counter(s)
        
        counterT=Counter(t)
        
        for x in set(t):
            if counterS[x] != counterT[x]:
                return x
