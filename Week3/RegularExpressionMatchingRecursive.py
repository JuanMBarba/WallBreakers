class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from collections import defaultdict
        memo = defaultdict(lambda:-1)
        
        lenS = len(s)
        lenP = len(p)
        skip = 0
        skipletter = ""
        if s == p:
            return True
        
        def _isMatch(iS, iP):
            
            if iS == lenS:
                if len(p[iP:])%2 == 0:
                    for x in range(iP+1,lenP,2):
                        if p[x] != "*":
                            return False
                    return True
                
                else:
                    return False
            
            im = iP != lenP and (s[iS] == p[iP] or p[iP] == ".")
            
            if memo[(iS,iP)] == -1:
                if iP+1 < lenP and p[iP+1] == "*":
                    memo[(iS,iP)] = _isMatch(iS, iP+2) or (im and _isMatch(iS+1, iP))
                else:
                    memo[(iS,iP)] = im and _isMatch(iS+1, iP+1)
            
            return memo[(iS,iP)]
        
        return _isMatch(0,0)
