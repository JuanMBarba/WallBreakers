class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictionary = {}
        
        lenS = len(s)
        lenT = len(t)
        
        if lenS != lenT:
            return False
        
        if lenS == 0 and lenT == 0:
            return True
        
        for x in range(lenS):
        
            try:
                dictionary[s[x]]+=1
            
            except:
                dictionary[s[x]] = 1
            
            try:
                dictionary[t[x]] -= 1
            
            except:
                dictionary[t[x]] =-1
            
            
        
        return list({*list(dictionary.values())}) == [0]
