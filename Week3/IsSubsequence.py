class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        lS = len(s)
        
        index = 0
        
        if s == "" or s == t:
            return True
        
        for letter in t:
            if s[index] == letter:
                index+=1
                if index == lS:
                    return True
        
        return False
