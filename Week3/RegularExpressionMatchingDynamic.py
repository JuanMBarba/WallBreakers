class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from collections import defaultdict
        memo = defaultdict(lambda:False)
        
        lenS = len(s)
        lenP = len(p)
        if s == p:
            return True
        memo[(lenS,lenP)]  = True
        for iS in range(lenS,-1,-1):
            for iP in range(lenP-1,-1,-1):
                if iS<lenS and(s[iS] == p[iP] or p[iP] == "."):
                    memo[(iS,iP)] = True

                if iP+1<lenP and p[iP+1]=="*":
                    memo[(iS,iP)] =  (memo[(iS,iP)]  and memo[(iS+1, iP)]) or memo[(iS,iP+2)] 
                else:
                    memo[(iS,iP)] = memo[(iS,iP)] and memo[(iS+1,iP+1)]
            
        return memo[(0,0)]
