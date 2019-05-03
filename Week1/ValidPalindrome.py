class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        simpleString = ''.join(x.lower() for x in s if x.isalnum())
        
        length = len(simpleString)
        
        for x in range(length//2):
            
            if simpleString[x] != simpleString[-1*(x+1)]:
                return False
        
        return True
