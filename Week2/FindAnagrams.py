class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        indices = []       
        
        lengthP = len(p)
        counterP = Counter(p)
        counterTemp = Counter()
        
        for x in range(len(s)-(lengthP-1)):
            if x == 0:
                counterTemp = Counter(s[x:x+lengthP])
            
            else:
                counterTemp[s[x-1]] = counterTemp[s[x-1]] - 1
                if counterTemp[s[x-1]] == 0:
                    del counterTemp[s[x-1]]
                counterTemp[s[x+lengthP-1]]+=1
                
            
            if counterTemp == counterP:
                indices.append(x)
            
        
        return indices
