class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        from collections import Counter
        
        sS = sorted(s)
        sG = sorted(g)
        
        result = 0
        
        while sS and sG:
            if sS[-1] >= sG[-1]:
                sS.pop()
                result+=1
            sG.pop()
        
        return result
